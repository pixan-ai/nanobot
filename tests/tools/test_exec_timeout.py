"""Tests for ExecTool timeout resolution (#3595).

Config-supplied timeouts are operator policy and not capped at runtime;
LLM-supplied tool-call timeouts are still bounded by ``_MAX_TIMEOUT`` to
match the tool-call schema and act as a guardrail against runaway agents.
``timeout=0`` in config disables the timeout entirely.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from nanobot.agent.tools.shell import ExecTool


def _mock_proc():
    """Return a mocked subprocess that completes immediately with empty output."""
    proc = AsyncMock()
    proc.communicate.return_value = (b"", b"")
    proc.returncode = 0
    return proc


async def _capture_wait_for_timeout(tool: ExecTool, *, tool_call_timeout=None):
    """Run ``tool.execute`` with subprocess and guard mocked, returning the
    ``timeout`` argument that ``asyncio.wait_for`` was called with.
    """
    proc = _mock_proc()

    async def fake_wait_for(coro, timeout):
        # Drain the coroutine so AsyncMock stays consistent.
        await coro
        fake_wait_for.captured = timeout
        return (b"", b"")

    fake_wait_for.captured = "unset"

    with (
        patch.object(ExecTool, "_spawn", AsyncMock(return_value=proc)),
        patch.object(ExecTool, "_guard_command", return_value=None),
        patch("nanobot.agent.tools.shell.asyncio.wait_for", side_effect=fake_wait_for),
    ):
        await tool.execute(command="echo hi", timeout=tool_call_timeout)

    return fake_wait_for.captured


@pytest.mark.asyncio
async def test_config_timeout_above_cap_is_not_truncated():
    """Config timeout of 1200s is honored, not truncated to _MAX_TIMEOUT (#3595)."""
    tool = ExecTool(timeout=1200)
    captured = await _capture_wait_for_timeout(tool)
    assert captured == 1200


@pytest.mark.asyncio
async def test_config_timeout_zero_disables_timeout():
    """Config timeout of 0 means no timeout: wait_for receives None (#3595)."""
    tool = ExecTool(timeout=0)
    captured = await _capture_wait_for_timeout(tool)
    assert captured is None


@pytest.mark.asyncio
async def test_tool_call_timeout_still_capped_at_max():
    """LLM-supplied tool-call timeout above _MAX_TIMEOUT is capped (regression guard)."""
    tool = ExecTool(timeout=60)
    captured = await _capture_wait_for_timeout(tool, tool_call_timeout=900)
    assert captured == ExecTool._MAX_TIMEOUT
