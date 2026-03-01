"""Tests for Telegram group_policy filtering."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from nanobot.channels.telegram import TelegramChannel
from nanobot.config.schema import TelegramConfig


def _make_channel(group_policy: str = "open") -> TelegramChannel:
    """Create a TelegramChannel with the given group_policy."""
    config = TelegramConfig(token="fake-token", group_policy=group_policy)
    bus = MagicMock()
    bus.publish_inbound = AsyncMock()
    channel = TelegramChannel(config=config, bus=bus)
    channel._bot_username = "testbot"
    channel._bot_id = 999
    channel._app = MagicMock()  # Pretend bot is running
    return channel


def _make_update(
    text: str = "hello",
    chat_type: str = "private",
    user_id: int = 123,
    username: str = "alice",
    reply_to_bot: bool = False,
    bot_id: int = 999,
) -> MagicMock:
    """Create a mock Telegram Update for testing."""
    user = MagicMock()
    user.id = user_id
    user.username = username
    user.first_name = "Alice"

    message = MagicMock()
    message.text = text
    message.caption = None
    message.chat_id = 1001
    message.chat.type = chat_type
    message.message_id = 42
    message.photo = []
    message.voice = None
    message.audio = None
    message.document = None
    message.media_group_id = None

    # Reply handling
    if reply_to_bot:
        reply_user = MagicMock()
        reply_user.id = bot_id
        reply_msg = MagicMock()
        reply_msg.from_user = reply_user
        message.reply_to_message = reply_msg
    else:
        message.reply_to_message = None

    update = MagicMock()
    update.message = message
    update.effective_user = user
    return update


@pytest.mark.asyncio
async def test_private_message_always_passes():
    """DMs should always be forwarded regardless of group_policy."""
    channel = _make_channel(group_policy="mention")
    update = _make_update(text="hello", chat_type="private")

    with patch.object(channel, "_handle_message", new_callable=AsyncMock) as mock_handle:
        await channel._on_message(update, MagicMock())
        mock_handle.assert_called_once()


@pytest.mark.asyncio
async def test_group_open_policy_always_passes():
    """group_policy='open' should forward all group messages."""
    channel = _make_channel(group_policy="open")
    update = _make_update(text="hello everyone", chat_type="group")

    with patch.object(channel, "_handle_message", new_callable=AsyncMock) as mock_handle:
        await channel._on_message(update, MagicMock())
        mock_handle.assert_called_once()


@pytest.mark.asyncio
async def test_group_mention_policy_skips_without_mention():
    """group_policy='mention' should skip messages without @mention or reply."""
    channel = _make_channel(group_policy="mention")
    update = _make_update(text="hello everyone", chat_type="group")

    with patch.object(channel, "_handle_message", new_callable=AsyncMock) as mock_handle:
        await channel._on_message(update, MagicMock())
        mock_handle.assert_not_called()


@pytest.mark.asyncio
async def test_group_mention_policy_passes_with_at_mention():
    """group_policy='mention' should forward messages containing @botusername."""
    channel = _make_channel(group_policy="mention")
    update = _make_update(text="hey @testbot what do you think?", chat_type="group")

    with patch.object(channel, "_handle_message", new_callable=AsyncMock) as mock_handle:
        await channel._on_message(update, MagicMock())
        mock_handle.assert_called_once()


@pytest.mark.asyncio
async def test_group_mention_policy_passes_with_reply_to_bot():
    """group_policy='mention' should forward messages that reply to the bot."""
    channel = _make_channel(group_policy="mention")
    update = _make_update(text="I agree", chat_type="group", reply_to_bot=True)

    with patch.object(channel, "_handle_message", new_callable=AsyncMock) as mock_handle:
        await channel._on_message(update, MagicMock())
        mock_handle.assert_called_once()
