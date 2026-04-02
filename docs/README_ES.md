<div align="center">
  <img src="../nanobot_logo.png" alt="nanobot" width="500">
  <h1>nanobot: Asistente Personal de IA Ultra-Ligero</h1>
  <p>
    <a href="https://pypi.org/project/nanobot-ai/"><img src="https://img.shields.io/pypi/v/nanobot-ai" alt="PyPI"></a>
    <a href="https://pepy.tech/project/nanobot-ai"><img src="https://static.pepy.tech/badge/nanobot-ai" alt="Descargas"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/licencia-MIT-green" alt="Licencia">
    <a href="../COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Grupo-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="../COMMUNICATION.md"><img src="https://img.shields.io/badge/WeChat-Grupo-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
    <a href="https://discord.gg/MnCvHqpUGB"><img src="https://img.shields.io/badge/Discord-Comunidad-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
  <p>
    <a href="../README.md">English</a> · <b>Español</b>
  </p>
</div>

🐈 **nanobot** es un asistente personal de IA **ultra-ligero** inspirado en [OpenClaw](https://github.com/openclaw/openclaw).

⚡️ Ofrece la funcionalidad principal de un agente con **99% menos líneas de código** que OpenClaw.

📏 Conteo de líneas en tiempo real: ejecuta `bash core_agent_lines.sh` para verificar en cualquier momento.

## 📢 Noticias

> [!IMPORTANT]
> **Nota de seguridad:** Debido al envenenamiento de la cadena de suministro de `litellm`, **revisa tu entorno Python lo antes posible** y consulta este [aviso](https://github.com/HKUDS/nanobot/discussions/2445) para más detalles. Hemos eliminado completamente `litellm` desde **v0.1.4.post6**.

- **2026-03-27** 🚀 Lanzamiento de **v0.1.4.post6** — desacoplamiento de arquitectura, eliminación de litellm, streaming de extremo a extremo, canal WeChat y una corrección de seguridad. Consulta las [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post6) para más detalles.
- **2026-03-26** 🏗️ Extracción del agent runner y unificación de hooks de ciclo de vida; coalescencia de stream delta en los límites.
- **2026-03-25** 🌏 Proveedor StepFun, zona horaria configurable, firmas de pensamiento Gemini.
- **2026-03-24** 🔧 Compatibilidad WeChat, streaming CardKit para Feishu, reestructuración de suite de tests.
- **2026-03-23** 🔧 Refactorización de enrutamiento de comandos para plugins, medios WhatsApp/WeChat, CLI unificado de login de canales.
- **2026-03-22** ⚡ Streaming de extremo a extremo, canal WeChat, optimización de caché Anthropic, comando `/status`.
- **2026-03-21** 🔒 Reemplazo de `litellm` por SDKs nativos `openai` + `anthropic`. Ver [commit](https://github.com/HKUDS/nanobot/commit/3dfdab7).
- **2026-03-20** 🧙 Asistente de configuración interactivo — elige tu proveedor, autocompletado de modelos, y listo.
- **2026-03-19** 💬 Telegram más resiliente bajo carga; Feishu ahora renderiza bloques de código correctamente.
- **2026-03-18** 📷 Telegram ahora puede enviar medios vía URL. Los schedules de Cron muestran detalles legibles.
- **2026-03-17** ✨ Mejoras de formato en Feishu, Slack reacciona al terminar, endpoints personalizados soportan headers extra, y manejo de imágenes más confiable.

<details>
<summary>Noticias anteriores</summary>

- **2026-03-16** 🚀 Lanzamiento de **v0.1.4.post5** — un release enfocado en refinamiento con mayor confiabilidad y soporte de canales, y una experiencia diaria más robusta. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post5).
- **2026-03-15** 🧩 Medios enriquecidos en DingTalk, skills integrados más inteligentes y compatibilidad de modelos más limpia.
- **2026-03-14** 💬 Plugins de canal, respuestas Feishu, y MCP, QQ y manejo de medios más estables.
- **2026-03-13** 🌐 Búsqueda web multi-proveedor, LangSmith y mejoras de confiabilidad generales.
- **2026-03-12** 🚀 Soporte VolcEngine, contexto de respuesta en Telegram, `/restart` y memoria más robusta.
- **2026-03-11** 🔌 WeCom, Ollama, descubrimiento más limpio y comportamiento de herramientas más seguro.
- **2026-03-10** 🧠 Memoria basada en tokens, reintentos compartidos y comportamiento más limpio del gateway y Telegram.
- **2026-03-09** 💬 Pulido de hilos en Slack y mejor compatibilidad de audio en Feishu.
- **2026-03-08** 🚀 Lanzamiento de **v0.1.4.post4** — un release repleto de confiabilidad con valores por defecto más seguros, mejor soporte multi-instancia, MCP más robusto y mejoras importantes en canales y proveedores. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post4).
- **2026-03-07** 🚀 Proveedor Azure OpenAI, medios WhatsApp, chats grupales QQ y más pulido en Telegram/Feishu.
- **2026-03-06** 🪄 Proveedores más ligeros, manejo de medios más inteligente y memoria y compatibilidad CLI más robustas.
- **2026-03-05** ⚡️ Borrador de streaming en Telegram, soporte MCP SSE y correcciones de confiabilidad en canales.
- **2026-03-04** 🛠️ Limpieza de dependencias, lecturas de archivos más seguras y otra ronda de correcciones de tests y Cron.
- **2026-03-03** 🧠 Fusión de mensajes de usuario más limpia, guardado multimodal más seguro y guardias de Cron más fuertes.
- **2026-03-02** 🛡️ Control de acceso por defecto más seguro, recargas de Cron más robustas y manejo de medios Matrix más limpio.
- **2026-03-01** 🌐 Soporte de proxy web, recordatorios de Cron más inteligentes y mejoras en el parseo de texto enriquecido de Feishu.
- **2026-02-28** 🚀 Lanzamiento de **v0.1.4.post3** — contexto más limpio, historial de sesión endurecido y agente más inteligente. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post3).
- **2026-02-27** 🧠 Soporte experimental de modo de pensamiento, mensajes multimedia en DingTalk, correcciones de canales Feishu y QQ.
- **2026-02-26** 🛡️ Corrección de envenenamiento de sesión, deduplicación WhatsApp, protección de rutas Windows, compatibilidad Mistral.
- **2026-02-25** 🧹 Nuevo canal Matrix, contexto de sesión más limpio, sincronización automática de plantillas de workspace.
- **2026-02-24** 🚀 Lanzamiento de **v0.1.4.post2** — un release enfocado en confiabilidad con heartbeat rediseñado, optimización de caché de prompts y estabilidad endurecida de proveedores y canales. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post2).
- **2026-02-23** 🔧 Heartbeat virtual de tool-call, optimización de caché de prompts, correcciones de mrkdwn en Slack.
- **2026-02-22** 🛡️ Aislamiento de hilos en Slack, corrección de typing en Discord, mejoras de confiabilidad del agente.
- **2026-02-21** 🎉 Lanzamiento de **v0.1.4.post1** — nuevos proveedores, soporte de medios en canales y mejoras importantes de estabilidad. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post1).
- **2026-02-20** 🐦 Feishu ahora recibe archivos multimodales de usuarios. Memoria más confiable bajo el capó.
- **2026-02-19** ✨ Slack ahora envía archivos, Discord divide mensajes largos y los subagentes funcionan en modo CLI.
- **2026-02-18** ⚡️ nanobot ahora soporta VolcEngine, headers de autenticación personalizada MCP y caché de prompts Anthropic.
- **2026-02-17** 🎉 Lanzamiento de **v0.1.4** — soporte MCP, streaming de progreso, nuevos proveedores y múltiples mejoras de canales. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4).
- **2026-02-16** 🦞 nanobot ahora integra un skill de [ClawHub](https://clawhub.ai) — busca e instala skills públicos de agentes.
- **2026-02-15** 🔑 nanobot ahora soporta proveedor OpenAI Codex con soporte de login OAuth.
- **2026-02-14** 🔌 ¡nanobot ahora soporta MCP! Ver [sección MCP](#mcp-model-context-protocol) para detalles.
- **2026-02-13** 🎉 Lanzamiento de **v0.1.3.post7** — incluye endurecimiento de seguridad y múltiples mejoras. **Por favor actualiza a la última versión para solucionar problemas de seguridad**. Ver [notas de lanzamiento](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post7).
- **2026-02-12** 🧠 Sistema de memoria rediseñado — Menos código, más confiable. ¡Únete a la [discusión](https://github.com/HKUDS/nanobot/discussions/566)!
- **2026-02-11** ✨ ¡Experiencia CLI mejorada y soporte MiniMax agregado!
- **2026-02-10** 🎉 Lanzamiento de **v0.1.3.post6** con mejoras. Revisa las [notas](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post6) y nuestro [roadmap](https://github.com/HKUDS/nanobot/discussions/431).
- **2026-02-09** 💬 ¡Soporte de Slack, Email y QQ agregado — nanobot ahora soporta múltiples plataformas de chat!
- **2026-02-08** 🔧 ¡Proveedores refactorizados — agregar un nuevo proveedor LLM ahora toma solo 2 simples pasos! Ver [aquí](#proveedores).
- **2026-02-07** 🚀 Lanzamiento de **v0.1.3.post5** con soporte Qwen y varias mejoras clave. Ver [aquí](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5).
- **2026-02-06** ✨ ¡Proveedor Moonshot/Kimi agregado, integración con Discord y endurecimiento de seguridad mejorado!
- **2026-02-05** ✨ ¡Canal Feishu, proveedor DeepSeek y soporte mejorado de tareas programadas!
- **2026-02-04** 🚀 Lanzamiento de **v0.1.3.post4** con soporte multi-proveedor y Docker. Ver [aquí](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post4).
- **2026-02-03** ⚡ ¡vLLM integrado para soporte LLM local y programación de tareas en lenguaje natural mejorada!
- **2026-02-02** 🎉 ¡nanobot lanzado oficialmente! Bienvenido a probar 🐈 nanobot!

</details>

> 🐈 nanobot es solo para fines educativos, de investigación e intercambio técnico. No está relacionado con criptomonedas y no involucra ningún token o moneda oficial.

## Características principales de nanobot:

🪶 **Ultra-Ligero**: Una implementación super ligera de OpenClaw — 99% más pequeña, significativamente más rápida.

🔬 **Listo para Investigación**: Código limpio y legible, fácil de entender, modificar y extender para investigación.

⚡️ **Veloz como un Rayo**: Mínima huella significa arranque más rápido, menor uso de recursos e iteraciones más rápidas.

💎 **Fácil de Usar**: Un clic para desplegar y estás listo.

## 🏗️ Arquitectura

<p align="center">
  <img src="../nanobot_arch.png" alt="arquitectura de nanobot" width="800">
</p>

## Tabla de Contenidos

- [Noticias](#-noticias)
- [Características principales](#características-principales-de-nanobot)
- [Arquitectura](#️-arquitectura)
- [Funcionalidades](#-funcionalidades)
- [Instalación](#-instalación)
- [Inicio Rápido](#-inicio-rápido)
- [Apps de Chat](#-apps-de-chat)
- [Red Social de Agentes](#-red-social-de-agentes)
- [Configuración](#️-configuración)
- [Múltiples Instancias](#-múltiples-instancias)
- [Referencia CLI](#-referencia-cli)
- [SDK Python](#-sdk-python)
- [API Compatible con OpenAI](#-api-compatible-con-openai)
- [Docker](#-docker)
- [Servicio Linux](#-servicio-linux)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribuir y Roadmap](#-contribuir--roadmap)
- [Historial de Estrellas](#-historial-de-estrellas)

## ✨ Funcionalidades

<table align="center">
  <tr align="center">
    <th><p align="center">📈 Análisis de Mercado en Tiempo Real 24/7</p></th>
    <th><p align="center">🚀 Ingeniero de Software Full-Stack</p></th>
    <th><p align="center">📅 Gestor de Rutina Diaria Inteligente</p></th>
    <th><p align="center">📚 Asistente de Conocimiento Personal</p></th>
  </tr>
  <tr>
    <td align="center"><p align="center"><img src="../case/search.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="../case/code.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="../case/scedule.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="../case/memory.gif" width="180" height="400"></p></td>
  </tr>
  <tr>
    <td align="center">Descubrimiento · Insights · Tendencias</td>
    <td align="center">Desarrollar · Desplegar · Escalar</td>
    <td align="center">Agendar · Automatizar · Organizar</td>
    <td align="center">Aprender · Memoria · Razonamiento</td>
  </tr>
</table>

## 📦 Instalación

**Instalar desde código fuente** (últimas funciones, recomendado para desarrollo)

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

**Instalar con [uv](https://github.com/astral-sh/uv)** (estable, rápido)

```bash
uv tool install nanobot-ai
```

**Instalar desde PyPI** (estable)

```bash
pip install nanobot-ai
```

### Actualizar a la última versión

**PyPI / pip**

```bash
pip install -U nanobot-ai
nanobot --version
```

**uv**

```bash
uv tool upgrade nanobot-ai
nanobot --version
```

**¿Usas WhatsApp?** Reconstruye el bridge local después de actualizar:

```bash
rm -rf ~/.nanobot/bridge
nanobot channels login whatsapp
```

## 🚀 Inicio Rápido

> [!TIP]
> Configura tu API key en `~/.nanobot/config.json`.
> Obtén API keys: [OpenRouter](https://openrouter.ai/keys) (Global)
>
> Para otros proveedores LLM, consulta la sección de [Proveedores](#proveedores).
>
> Para configurar búsqueda web, consulta [Búsqueda Web](#búsqueda-web).

**1. Inicializar**

```bash
nanobot onboard
```

Usa `nanobot onboard --wizard` si quieres el asistente de configuración interactivo.

**2. Configurar** (`~/.nanobot/config.json`)

Configura estas **dos partes** en tu config (las demás opciones tienen valores por defecto).

*Configura tu API key* (ej. OpenRouter, recomendado para usuarios globales):
```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  }
}
```

*Configura tu modelo* (opcionalmente fija un proveedor — por defecto es auto-detección):
```json
{
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5",
      "provider": "openrouter"
    }
  }
}
```

**3. Chatear**

```bash
nanobot agent
```

¡Eso es todo! Tienes un asistente de IA funcionando en 2 minutos.

## 💬 Apps de Chat

Conecta nanobot a tu plataforma de chat favorita. ¿Quieres construir la tuya propia? Consulta la [Guía de Plugins de Canal](./CHANNEL_PLUGIN_GUIDE.md).

| Canal | Lo que necesitas |
|-------|-----------------|
| **Telegram** | Token de bot de @BotFather |
| **Discord** | Token de bot + Message Content intent |
| **WhatsApp** | Escaneo de código QR (`nanobot channels login whatsapp`) |
| **WeChat (Weixin)** | Escaneo de código QR (`nanobot channels login weixin`) |
| **Feishu** | App ID + App Secret |
| **DingTalk** | App Key + App Secret |
| **Slack** | Bot token + App-Level token |
| **Matrix** | URL del Homeserver + Access token |
| **Email** | Credenciales IMAP/SMTP |
| **QQ** | App ID + App Secret |
| **Wecom** | Bot ID + Bot Secret |
| **Mochat** | Token Claw (configuración automática disponible) |

<details>
<summary><b>Telegram</b> (Recomendado)</summary>

**1. Crear un bot**
- Abre Telegram, busca `@BotFather`
- Envía `/newbot`, sigue las instrucciones
- Copia el token

**2. Configurar**

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "TU_TOKEN_DE_BOT",
      "allowFrom": ["TU_USER_ID"]
    }
  }
}
```

> Puedes encontrar tu **User ID** en la configuración de Telegram. Se muestra como `@tuUserId`.
> Copia este valor **sin el símbolo `@`** y pégalo en el archivo de configuración.

**3. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Mochat (Claw IM)</b></summary>

Usa **WebSocket Socket.IO** por defecto, con respaldo a polling HTTP.

**1. Pide a nanobot que configure Mochat por ti**

Simplemente envía este mensaje a nanobot (reemplaza `xxx@xxx` con tu email real):

```
Read https://raw.githubusercontent.com/HKUDS/MoChat/refs/heads/main/skills/nanobot/skill.md and register on MoChat. My Email account is xxx@xxx Bind me as your owner and DM me on MoChat.
```

nanobot se registrará automáticamente, configurará `~/.nanobot/config.json` y se conectará a Mochat.

**2. Reiniciar gateway**

```bash
nanobot gateway
```

¡Eso es todo — nanobot se encarga del resto!

<details>
<summary>Configuración manual (avanzado)</summary>

Si prefieres configurar manualmente, agrega lo siguiente a `~/.nanobot/config.json`:

> Mantén `claw_token` privado. Solo debe enviarse en el header `X-Claw-Token` a tu endpoint de API de Mochat.

```json
{
  "channels": {
    "mochat": {
      "enabled": true,
      "base_url": "https://mochat.io",
      "socket_url": "https://mochat.io",
      "socket_path": "/socket.io",
      "claw_token": "claw_xxx",
      "agent_user_id": "6982abcdef",
      "sessions": ["*"],
      "panels": ["*"],
      "reply_delay_mode": "non-mention",
      "reply_delay_ms": 120000
    }
  }
}
```

</details>

</details>

<details>
<summary><b>Discord</b></summary>

**1. Crear un bot**
- Ve a https://discord.com/developers/applications
- Crea una aplicación → Bot → Add Bot
- Copia el token del bot

**2. Habilitar intents**
- En la configuración del Bot, habilita **MESSAGE CONTENT INTENT**
- (Opcional) Habilita **SERVER MEMBERS INTENT** si planeas usar listas de permitidos basadas en datos de miembros

**3. Obtener tu User ID**
- Configuración de Discord → Avanzado → habilita **Modo Desarrollador**
- Clic derecho en tu avatar → **Copiar ID de usuario**

**4. Configurar**

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "TU_TOKEN_DE_BOT",
      "allowFrom": ["TU_USER_ID"],
      "groupPolicy": "mention"
    }
  }
}
```

> `groupPolicy` controla cómo responde el bot en canales de grupo:
> - `"mention"` (por defecto) — Solo responde cuando se le @menciona
> - `"open"` — Responde a todos los mensajes
> Los DMs siempre responden cuando el remitente está en `allowFrom`.

**5. Invitar al bot**
- OAuth2 → URL Generator
- Scopes: `bot`
- Permisos del Bot: `Send Messages`, `Read Message History`
- Abre la URL generada e invita al bot a tu servidor

**6. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Matrix (Element)</b></summary>

Instala las dependencias de Matrix primero:

```bash
pip install nanobot-ai[matrix]
```

**1. Crear/elegir una cuenta Matrix**

- Crea o reutiliza una cuenta Matrix en tu homeserver (por ejemplo `matrix.org`).
- Confirma que puedes iniciar sesión con Element.

**2. Obtener credenciales**

- Necesitas:
  - `userId` (ejemplo: `@nanobot:matrix.org`)
  - `accessToken`
  - `deviceId` (recomendado para poder restaurar tokens de sincronización entre reinicios)

**3. Configurar**

```json
{
  "channels": {
    "matrix": {
      "enabled": true,
      "homeserver": "https://matrix.org",
      "userId": "@nanobot:matrix.org",
      "accessToken": "syt_xxx",
      "deviceId": "NANOBOT01",
      "e2eeEnabled": true,
      "allowFrom": ["@tu_usuario:matrix.org"],
      "groupPolicy": "open",
      "groupAllowFrom": [],
      "allowRoomMentions": false,
      "maxMediaBytes": 20971520
    }
  }
}
```

| Opción | Descripción |
|--------|-------------|
| `allowFrom` | IDs de usuario permitidos. Vacío deniega todo; usa `["*"]` para permitir a todos. |
| `groupPolicy` | `open` (por defecto), `mention`, o `allowlist`. |
| `groupAllowFrom` | Lista de salas permitidas (cuando la política es `allowlist`). |
| `allowRoomMentions` | Aceptar menciones `@room` en modo mention. |
| `e2eeEnabled` | Soporte E2EE (por defecto `true`). Configura `false` para solo texto plano. |
| `maxMediaBytes` | Tamaño máximo de adjuntos (por defecto `20MB`). Configura `0` para bloquear todo media. |

**4. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>WhatsApp</b></summary>

Requiere **Node.js ≥18**.

**1. Vincular dispositivo**

```bash
nanobot channels login whatsapp
# Escanea el QR con WhatsApp → Configuración → Dispositivos Vinculados
```

**2. Configurar**

```json
{
  "channels": {
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["+521234567890"]
    }
  }
}
```

**3. Ejecutar** (dos terminales)

```bash
# Terminal 1
nanobot channels login whatsapp

# Terminal 2
nanobot gateway
```

> Las actualizaciones del bridge de WhatsApp no se aplican automáticamente para instalaciones existentes.
> Después de actualizar nanobot, reconstruye el bridge local con:
> `rm -rf ~/.nanobot/bridge && nanobot channels login whatsapp`

</details>

<details>
<summary><b>Feishu</b></summary>

Usa conexión larga **WebSocket** — no se requiere IP pública.

**1. Crear un bot de Feishu**
- Visita [Feishu Open Platform](https://open.feishu.cn/app)
- Crea una nueva app → Habilita la capacidad de **Bot**
- **Permisos**:
  - `im:message` (enviar mensajes) e `im:message.p2p_msg:readonly` (recibir mensajes)
  - **Respuestas con streaming**: agrega **`cardkit:card:write`** (frecuentemente etiquetado como **Crear y actualizar tarjetas** en la consola de desarrollador de Feishu). Requerido para entidades CardKit y texto de asistente con streaming.
  - Si **no puedes** agregar `cardkit:card:write`, configura `"streaming": false` bajo `channels.feishu`. El bot sigue funcionando; las respuestas usan tarjetas interactivas normales sin streaming token por token.
- **Eventos**: Agrega `im.message.receive_v1` (recibir mensajes)
  - Selecciona modo **Long Connection** (requiere ejecutar nanobot primero para establecer conexión)
- Obtén **App ID** y **App Secret** de "Credentials & Basic Info"
- Publica la app

**2. Configurar**

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxx",
      "appSecret": "xxx",
      "encryptKey": "",
      "verificationToken": "",
      "allowFrom": ["ou_TU_OPEN_ID"],
      "groupPolicy": "mention",
      "streaming": true
    }
  }
}
```

> `streaming` por defecto es `true`. Usa `false` si tu app no tiene **`cardkit:card:write`** (ver permisos arriba).
> `encryptKey` y `verificationToken` son opcionales para modo Long Connection.
> `allowFrom`: Agrega tu open_id (encuéntralo en los logs de nanobot cuando le envíes un mensaje al bot). Usa `["*"]` para permitir a todos.
> `groupPolicy`: `"mention"` (por defecto — responde solo cuando se le @menciona), `"open"` (responde a todos los mensajes del grupo). Los chats privados siempre responden.

**3. Ejecutar**

```bash
nanobot gateway
```

> [!TIP]
> ¡Feishu usa WebSocket para recibir mensajes — no se necesita webhook ni IP pública!

</details>

<details>
<summary><b>QQ (QQ Chats privados)</b></summary>

Usa **SDK botpy** con WebSocket — no se requiere IP pública. Actualmente soporta **solo mensajes privados**.

**1. Registrarse y crear bot**
- Visita [QQ Open Platform](https://q.qq.com) → Regístrate como desarrollador
- Crea una nueva aplicación de bot
- Ve a **开发设置 (Developer Settings)** → copia **AppID** y **AppSecret**

**2. Configurar sandbox para testing**
- En la consola de administración del bot, encuentra **沙箱配置 (Sandbox Config)**
- Agrega tu propio número QQ
- Escanea el código QR del bot con QQ móvil → abre el perfil del bot → toca "发消息" para empezar a chatear

**3. Configurar**

```json
{
  "channels": {
    "qq": {
      "enabled": true,
      "appId": "TU_APP_ID",
      "secret": "TU_APP_SECRET",
      "allowFrom": ["TU_OPENID"],
      "msgFormat": "plain"
    }
  }
}
```

**4. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>DingTalk (钉钉)</b></summary>

Usa **Stream Mode** — no se requiere IP pública.

**1. Crear un bot de DingTalk**
- Visita [DingTalk Open Platform](https://open-dev.dingtalk.com/)
- Crea una nueva app → Agrega capacidad de **Robot**
- **Configuración**: Activa **Stream Mode**
- **Permisos**: Agrega los permisos necesarios para enviar mensajes
- Obtén **AppKey** (Client ID) y **AppSecret** (Client Secret) de "Credentials"
- Publica la app

**2. Configurar**

```json
{
  "channels": {
    "dingtalk": {
      "enabled": true,
      "clientId": "TU_APP_KEY",
      "clientSecret": "TU_APP_SECRET",
      "allowFrom": ["TU_STAFF_ID"]
    }
  }
}
```

> `allowFrom`: Agrega tu staff ID. Usa `["*"]` para permitir a todos.

**3. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Slack</b></summary>

Usa **Socket Mode** — no se requiere URL pública.

**1. Crear una app de Slack**
- Ve a [Slack API](https://api.slack.com/apps) → **Create New App** → "From scratch"
- Elige un nombre y selecciona tu workspace

**2. Configurar la app**
- **Socket Mode**: Activa → Genera un **App-Level Token** con scope `connections:write` → cópialo (`xapp-...`)
- **OAuth & Permissions**: Agrega bot scopes: `chat:write`, `reactions:write`, `app_mentions:read`
- **Event Subscriptions**: Activa → Suscríbete a bot events: `message.im`, `message.channels`, `app_mention` → Guarda Cambios
- **App Home**: Ve a **Show Tabs** → Habilita **Messages Tab** → Marca **"Allow users to send Slash commands and messages from the messages tab"**
- **Install App**: Click **Install to Workspace** → Autoriza → copia el **Bot Token** (`xoxb-...`)

**3. Configurar nanobot**

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "botToken": "xoxb-...",
      "appToken": "xapp-...",
      "allowFrom": ["TU_SLACK_USER_ID"],
      "groupPolicy": "mention"
    }
  }
}
```

**4. Ejecutar**

```bash
nanobot gateway
```

¡Envía un DM al bot directamente o @menciónalo en un canal — debería responder!

> [!TIP]
> - `groupPolicy`: `"mention"` (por defecto — responde solo cuando se le @menciona), `"open"` (responde a todos los mensajes del canal), o `"allowlist"` (restringe a canales específicos).
> - La política de DM es open por defecto. Configura `"dm": {"enabled": false}` para deshabilitar DMs.

</details>

<details>
<summary><b>Email</b></summary>

Dale a nanobot su propia cuenta de email. Revisa **IMAP** para correos entrantes y responde vía **SMTP** — como un asistente personal de email.

**1. Obtener credenciales (ejemplo con Gmail)**
- Crea una cuenta de Gmail dedicada para tu bot (ej. `mi-nanobot@gmail.com`)
- Habilita Verificación en 2 Pasos → Crea una [Contraseña de Aplicación](https://myaccount.google.com/apppasswords)
- Usa esta contraseña de aplicación tanto para IMAP como para SMTP

**2. Configurar**

> - `consentGranted` debe ser `true` para permitir el acceso al buzón. Esta es una puerta de seguridad — configura `false` para deshabilitar completamente.
> - `allowFrom`: Agrega tu dirección de email. Usa `["*"]` para aceptar emails de cualquiera.
> - Configura `"autoReplyEnabled": false` si solo quieres leer/analizar emails sin enviar respuestas automáticas.

```json
{
  "channels": {
    "email": {
      "enabled": true,
      "consentGranted": true,
      "imapHost": "imap.gmail.com",
      "imapPort": 993,
      "imapUsername": "mi-nanobot@gmail.com",
      "imapPassword": "tu-contraseña-de-app",
      "smtpHost": "smtp.gmail.com",
      "smtpPort": 587,
      "smtpUsername": "mi-nanobot@gmail.com",
      "smtpPassword": "tu-contraseña-de-app",
      "fromAddress": "mi-nanobot@gmail.com",
      "allowFrom": ["tu-email-real@gmail.com"]
    }
  }
}
```

**3. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>WeChat (微信 / Weixin)</b></summary>

Usa **HTTP long-poll** con login por código QR vía la API personal WeChat de ilinkai. No se requiere cliente de escritorio de WeChat.

**1. Instalar con soporte WeChat**

```bash
pip install "nanobot-ai[weixin]"
```

**2. Configurar**

```json
{
  "channels": {
    "weixin": {
      "enabled": true,
      "allowFrom": ["TU_WECHAT_USER_ID"]
    }
  }
}
```

> - `allowFrom`: Agrega el sender ID que ves en los logs de nanobot para tu cuenta de WeChat. Usa `["*"]` para permitir a todos.
> - `token`: Opcional. Si se omite, inicia sesión interactivamente y nanobot guardará el token por ti.

**3. Iniciar sesión**

```bash
nanobot channels login weixin
```

Usa `--force` para re-autenticar e ignorar cualquier token guardado:

```bash
nanobot channels login weixin --force
```

**4. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Wecom (企业微信)</b></summary>

> Aquí usamos [wecom-aibot-sdk-python](https://github.com/chengyongru/wecom_aibot_sdk) (versión Python comunitaria del SDK oficial [@wecom/aibot-node-sdk](https://www.npmjs.com/package/@wecom/aibot-node-sdk)).
>
> Usa conexión larga **WebSocket** — no se requiere IP pública.

**1. Instalar la dependencia opcional**

```bash
pip install nanobot-ai[wecom]
```

**2. Crear un Bot IA de WeCom**

Ve a la consola de administración de WeCom → Robot Inteligente → Crear Robot → selecciona modo **API** con **long connection**. Copia el Bot ID y Secret.

**3. Configurar**

```json
{
  "channels": {
    "wecom": {
      "enabled": true,
      "botId": "tu_bot_id",
      "secret": "tu_bot_secret",
      "allowFrom": ["tu_id"]
    }
  }
}
```

**4. Ejecutar**

```bash
nanobot gateway
```

</details>

## 🌐 Red Social de Agentes

🐈 nanobot es capaz de conectarse a la red social de agentes (comunidad de agentes). **¡Solo envía un mensaje y tu nanobot se une automáticamente!**

| Plataforma | Cómo unirse (envía este mensaje a tu bot) |
|------------|------------------------------------------|
| [**Moltbook**](https://www.moltbook.com/) | `Read https://moltbook.com/skill.md and follow the instructions to join Moltbook` |
| [**ClawdChat**](https://clawdchat.ai/) | `Read https://clawdchat.ai/skill.md and follow the instructions to join ClawdChat` |

Simplemente envía el comando de arriba a tu nanobot (vía CLI o cualquier canal de chat), y él se encargará del resto.

## ⚙️ Configuración

Archivo de configuración: `~/.nanobot/config.json`

### Proveedores

> [!TIP]
> - **Groq** proporciona transcripción de voz gratuita vía Whisper. Si está configurado, los mensajes de voz de Telegram se transcribirán automáticamente.
> - **MiniMax Plan Coding**: Enlaces de descuento exclusivos para la comunidad nanobot: [Internacional](https://platform.minimax.io/subscribe/coding-plan?code=9txpdXw04g&source=link) · [China Continental](https://platform.minimaxi.com/subscribe/token-plan?code=GILTJpMTqZ&source=link)
> - **MiniMax (China Continental)**: Si tu API key es de la plataforma de China Continental de MiniMax (minimaxi.com), configura `"apiBase": "https://api.minimaxi.com/v1"` en tu config del proveedor minimax.
> - **VolcEngine / BytePlus Plan Coding**: Usa los proveedores dedicados `volcengineCodingPlan` o `byteplusCodingPlan` en lugar de los proveedores de pago por uso `volcengine` / `byteplus`.
> - **Zhipu Plan Coding**: Si estás en el plan coding de Zhipu, configura `"apiBase": "https://open.bigmodel.cn/api/coding/paas/v4"` en tu config del proveedor zhipu.
> - **Alibaba Cloud BaiLian**: Si usas el endpoint compatible con OpenAI de Alibaba Cloud BaiLian, configura `"apiBase": "https://dashscope.aliyuncs.com/compatible-mode/v1"` en tu config del proveedor dashscope.
> - **Step Fun (China Continental)**: Si tu API key es de la plataforma de China Continental de Step Fun (stepfun.com), configura `"apiBase": "https://api.stepfun.com/v1"` en tu config del proveedor stepfun.

| Proveedor | Propósito | Obtener API Key |
|-----------|-----------|----------------|
| `custom` | Cualquier endpoint compatible con OpenAI | — |
| `openrouter` | LLM (recomendado, acceso a todos los modelos) | [openrouter.ai](https://openrouter.ai) |
| `volcengine` | LLM (VolcEngine, pago por uso) | [Plan Coding](https://www.volcengine.com/activity/codingplan?utm_campaign=nanobot&utm_content=nanobot&utm_medium=devrel&utm_source=OWO&utm_term=nanobot) · [volcengine.com](https://www.volcengine.com) |
| `byteplus` | LLM (VolcEngine internacional, pago por uso) | [Plan Coding](https://www.byteplus.com/en/activity/codingplan?utm_campaign=nanobot&utm_content=nanobot&utm_medium=devrel&utm_source=OWO&utm_term=nanobot) · [byteplus.com](https://www.byteplus.com) |
| `anthropic` | LLM (Claude directo) | [console.anthropic.com](https://console.anthropic.com) |
| `azure_openai` | LLM (Azure OpenAI) | [portal.azure.com](https://portal.azure.com) |
| `openai` | LLM (GPT directo) | [platform.openai.com](https://platform.openai.com) |
| `deepseek` | LLM (DeepSeek directo) | [platform.deepseek.com](https://platform.deepseek.com) |
| `groq` | LLM + **Transcripción de voz** (Whisper) | [console.groq.com](https://console.groq.com) |
| `minimax` | LLM (MiniMax directo) | [platform.minimaxi.com](https://platform.minimaxi.com) |
| `gemini` | LLM (Gemini directo) | [aistudio.google.com](https://aistudio.google.com) |
| `aihubmix` | LLM (gateway API, acceso a todos los modelos) | [aihubmix.com](https://aihubmix.com) |
| `siliconflow` | LLM (SiliconFlow/硅基流动) | [siliconflow.cn](https://siliconflow.cn) |
| `dashscope` | LLM (Qwen) | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) |
| `moonshot` | LLM (Moonshot/Kimi) | [platform.moonshot.cn](https://platform.moonshot.cn) |
| `zhipu` | LLM (Zhipu GLM) | [open.bigmodel.cn](https://open.bigmodel.cn) |
| `ollama` | LLM (local, Ollama) | — |
| `mistral` | LLM | [docs.mistral.ai](https://docs.mistral.ai/) |
| `stepfun` | LLM (Step Fun/阶跃星辰) | [platform.stepfun.com](https://platform.stepfun.com) |
| `ovms` | LLM (local, OpenVINO Model Server) | [docs.openvino.ai](https://docs.openvino.ai/2026/model-server/ovms_docs_llm_quickstart.html) |
| `vllm` | LLM (local, cualquier servidor compatible con OpenAI) | — |
| `openai_codex` | LLM (Codex, OAuth) | `nanobot provider login openai-codex` |
| `github_copilot` | LLM (GitHub Copilot, OAuth) | `nanobot provider login github-copilot` |

<details>
<summary><b>OpenAI Codex (OAuth)</b></summary>

Codex usa OAuth en lugar de API keys. Requiere una cuenta ChatGPT Plus o Pro.
No se necesita bloque `providers.openaiCodex` en `config.json`; `nanobot provider login` almacena la sesión OAuth fuera del config.

**1. Iniciar sesión:**
```bash
nanobot provider login openai-codex
```

**2. Configurar modelo** (fusionar en `~/.nanobot/config.json`):
```json
{
  "agents": {
    "defaults": {
      "model": "openai-codex/gpt-5.1-codex"
    }
  }
}
```

**3. Chatear:**
```bash
nanobot agent -m "¡Hola!"
```

> Usuarios de Docker: usa `docker run -it` para login OAuth interactivo.

</details>

<details>
<summary><b>GitHub Copilot (OAuth)</b></summary>

GitHub Copilot usa OAuth en lugar de API keys. Requiere una [cuenta de GitHub con plan configurado](https://github.com/features/copilot/plans).
No se necesita bloque `providers.githubCopilot` en `config.json`; `nanobot provider login` almacena la sesión OAuth fuera del config.

**1. Iniciar sesión:**
```bash
nanobot provider login github-copilot
```

**2. Configurar modelo** (fusionar en `~/.nanobot/config.json`):
```json
{
  "agents": {
    "defaults": {
      "model": "github-copilot/gpt-4.1"
    }
  }
}
```

**3. Chatear:**
```bash
nanobot agent -m "¡Hola!"
```

> Usuarios de Docker: usa `docker run -it` para login OAuth interactivo.

</details>

<details>
<summary><b>Proveedor Personalizado (Cualquier API compatible con OpenAI)</b></summary>

Se conecta directamente a cualquier endpoint compatible con OpenAI — LM Studio, llama.cpp, Together AI, Fireworks, Azure OpenAI, o cualquier servidor auto-hospedado. El nombre del modelo se pasa tal cual.

```json
{
  "providers": {
    "custom": {
      "apiKey": "tu-api-key",
      "apiBase": "https://api.tu-proveedor.com/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "nombre-de-tu-modelo"
    }
  }
}
```

> Para servidores locales que no requieren key, configura `apiKey` como cualquier string no vacío (ej. `"no-key"`).

</details>

<details>
<summary><b>Ollama (local)</b></summary>

Ejecuta un modelo local con Ollama, luego agrega a config:

**1. Iniciar Ollama** (ejemplo):
```bash
ollama run llama3.2
```

**2. Agregar a config** (parcial — fusionar en `~/.nanobot/config.json`):
```json
{
  "providers": {
    "ollama": {
      "apiBase": "http://localhost:11434"
    }
  },
  "agents": {
    "defaults": {
      "provider": "ollama",
      "model": "llama3.2"
    }
  }
}
```

> `provider: "auto"` también funciona cuando `providers.ollama.apiBase` está configurado, pero configurar `"provider": "ollama"` es la opción más clara.

</details>

<details>
<summary><b>OpenVINO Model Server (local / compatible con OpenAI)</b></summary>

Ejecuta LLMs localmente en GPUs Intel usando [OpenVINO Model Server](https://docs.openvino.ai/2026/model-server/ovms_docs_llm_quickstart.html). OVMS expone una API compatible con OpenAI en `/v3`.

> Requiere Docker y una GPU Intel con acceso al driver (`/dev/dri`).

**1. Descargar el modelo** (ejemplo):

```bash
mkdir -p ov/models && cd ov

docker run -d \
  --rm \
  --user $(id -u):$(id -g) \
  -v $(pwd)/models:/models \
  openvino/model_server:latest-gpu \
  --pull \
  --model_name openai/gpt-oss-20b \
  --model_repository_path /models \
  --source_model OpenVINO/gpt-oss-20b-int4-ov \
  --task text_generation \
  --tool_parser gptoss \
  --reasoning_parser gptoss \
  --enable_prefix_caching true \
  --target_device GPU
```

**2. Iniciar el servidor** (ejemplo):

```bash
docker run -d \
  --rm \
  --name ovms \
  --user $(id -u):$(id -g) \
  -p 8000:8000 \
  -v $(pwd)/models:/models \
  --device /dev/dri \
  --group-add=$(stat -c "%g" /dev/dri/render* | head -n 1) \
  openvino/model_server:latest-gpu \
  --rest_port 8000 \
  --model_name openai/gpt-oss-20b \
  --model_repository_path /models \
  --source_model OpenVINO/gpt-oss-20b-int4-ov \
  --task text_generation \
  --tool_parser gptoss \
  --reasoning_parser gptoss \
  --enable_prefix_caching true \
  --target_device GPU
```

**3. Agregar a config** (parcial — fusionar en `~/.nanobot/config.json`):

```json
{
  "providers": {
    "ovms": {
      "apiBase": "http://localhost:8000/v3"
    }
  },
  "agents": {
    "defaults": {
      "provider": "ovms",
      "model": "openai/gpt-oss-20b"
    }
  }
}
```

> OVMS es un servidor local — no se requiere API key. Soporta llamadas a herramientas (`--tool_parser gptoss`), razonamiento (`--reasoning_parser gptoss`) y streaming.

</details>

<details>
<summary><b>vLLM (local / compatible con OpenAI)</b></summary>

Ejecuta tu propio modelo con vLLM o cualquier servidor compatible con OpenAI, luego agrega a config:

**1. Iniciar el servidor** (ejemplo):
```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

**2. Agregar a config** (parcial — fusionar en `~/.nanobot/config.json`):

*Proveedor (key puede ser cualquier string no vacío para local):*
```json
{
  "providers": {
    "vllm": {
      "apiKey": "dummy",
      "apiBase": "http://localhost:8000/v1"
    }
  }
}
```

*Modelo:*
```json
{
  "agents": {
    "defaults": {
      "model": "meta-llama/Llama-3.1-8B-Instruct"
    }
  }
}
```

</details>

<details>
<summary><b>Agregar un Nuevo Proveedor (Guía para Desarrolladores)</b></summary>

nanobot usa un **Provider Registry** (`nanobot/providers/registry.py`) como única fuente de verdad.
Agregar un nuevo proveedor solo toma **2 pasos** — sin cadenas if-elif que tocar.

**Paso 1.** Agrega una entrada `ProviderSpec` a `PROVIDERS` en `nanobot/providers/registry.py`:

```python
ProviderSpec(
    name="miprovider",                    # nombre del campo de config
    keywords=("miprovider", "mimodelo"),  # keywords del nombre del modelo para auto-matching
    env_key="MIPROVIDER_API_KEY",         # nombre de variable de entorno
    display_name="Mi Proveedor",          # mostrado en `nanobot status`
    default_api_base="https://api.miprovider.com/v1",  # endpoint compatible con OpenAI
)
```

**Paso 2.** Agrega un campo a `ProvidersConfig` en `nanobot/config/schema.py`:

```python
class ProvidersConfig(BaseModel):
    ...
    miprovider: ProviderConfig = ProviderConfig()
```

¡Eso es todo! Variables de entorno, enrutamiento de modelos, matching de config, y visualización en `nanobot status` funcionarán automáticamente.

**Opciones comunes de `ProviderSpec`:**

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `default_api_base` | URL base compatible con OpenAI | `"https://api.deepseek.com"` |
| `env_extras` | Variables de entorno adicionales a configurar | `(("ZHIPUAI_API_KEY", "{api_key}"),)` |
| `model_overrides` | Overrides de parámetros por modelo | `(("kimi-k2.5", {"temperature": 1.0}),)` |
| `is_gateway` | Puede enrutar cualquier modelo (como OpenRouter) | `True` |
| `detect_by_key_prefix` | Detectar gateway por prefijo de API key | `"sk-or-"` |
| `detect_by_base_keyword` | Detectar gateway por URL base de API | `"openrouter"` |
| `strip_model_prefix` | Eliminar prefijo del proveedor antes de enviar al gateway | `True` (para AiHubMix) |
| `supports_max_completion_tokens` | Usar `max_completion_tokens` en lugar de `max_tokens` | `True` |

</details>

### Configuración de Canales

Configuración global que aplica a todos los canales. Configura bajo la sección `channels` en `~/.nanobot/config.json`:

```json
{
  "channels": {
    "sendProgress": true,
    "sendToolHints": false,
    "sendMaxRetries": 3,
    "telegram": { ... }
  }
}
```

| Configuración | Por defecto | Descripción |
|---------------|-------------|-------------|
| `sendProgress` | `true` | Transmitir el progreso del texto del agente al canal |
| `sendToolHints` | `false` | Transmitir hints de llamadas a herramientas (ej. `read_file("…")`) |
| `sendMaxRetries` | `3` | Máximo de intentos de entrega por mensaje saliente, incluyendo el envío inicial (0-10 configurado, mínimo 1 intento real) |

#### Comportamiento de Reintentos

Cuando una operación de envío de canal lanza un error, nanobot reintenta con backoff exponencial:

- **Intento 1**: Envío inicial
- **Intentos 2-4**: Demoras de reintento son 1s, 2s, 4s
- **Intentos 5+**: La demora de reintento se limita a 4s
- **Fallos transitorios** (problemas de red, límites temporales de API): El reintento generalmente tiene éxito
- **Fallos permanentes** (token inválido, canal baneado): Todos los reintentos fallan

> [!NOTE]
> Cuando un canal está completamente no disponible, no hay forma de notificar al usuario ya que no podemos contactarlo a través de ese canal. Monitorea los logs para "Failed to send to {channel} after N attempts" para detectar fallos persistentes de entrega.

### Búsqueda Web

> [!TIP]
> Usa `proxy` en `tools.web` para enrutar todas las solicitudes web (búsqueda + fetch) a través de un proxy:
> ```json
> { "tools": { "web": { "proxy": "http://127.0.0.1:7890" } } }
> ```

nanobot soporta múltiples proveedores de búsqueda web. Configura en `~/.nanobot/config.json` bajo `tools.web.search`.

| Proveedor | Campos de config | Env var de respaldo | Gratuito |
|-----------|-----------------|---------------------|----------|
| `brave` (por defecto) | `apiKey` | `BRAVE_API_KEY` | No |
| `tavily` | `apiKey` | `TAVILY_API_KEY` | No |
| `jina` | `apiKey` | `JINA_API_KEY` | Nivel gratuito (10M tokens) |
| `searxng` | `baseUrl` | `SEARXNG_BASE_URL` | Sí (auto-hospedado) |
| `duckduckgo` | — | — | Sí |

Cuando faltan credenciales, nanobot automáticamente usa DuckDuckGo.

**Brave** (por defecto):
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "brave",
        "apiKey": "BSA..."
      }
    }
  }
}
```

**Tavily:**
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "tavily",
        "apiKey": "tvly-..."
      }
    }
  }
}
```

**Jina** (nivel gratuito con 10M tokens):
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "jina",
        "apiKey": "jina_..."
      }
    }
  }
}
```

**SearXNG** (auto-hospedado, sin API key necesaria):
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "searxng",
        "baseUrl": "https://searx.ejemplo"
      }
    }
  }
}
```

**DuckDuckGo** (sin configuración):
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "duckduckgo"
      }
    }
  }
}
```

| Opción | Tipo | Por defecto | Descripción |
|--------|------|-------------|-------------|
| `provider` | string | `"brave"` | Backend de búsqueda: `brave`, `tavily`, `jina`, `searxng`, `duckduckgo` |
| `apiKey` | string | `""` | API key para Brave o Tavily |
| `baseUrl` | string | `""` | URL base para SearXNG |
| `maxResults` | integer | `5` | Resultados por búsqueda (1–10) |

### MCP (Model Context Protocol)

> [!TIP]
> El formato de configuración es compatible con Claude Desktop / Cursor. Puedes copiar las configuraciones de servidores MCP directamente de cualquier README de servidor MCP.

nanobot soporta [MCP](https://modelcontextprotocol.io/) — conecta servidores de herramientas externos y úsalos como herramientas nativas del agente.

Agrega servidores MCP a tu `config.json`:

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/ruta/al/dir"]
      },
      "mi-mcp-remoto": {
        "url": "https://ejemplo.com/mcp/",
        "headers": {
          "Authorization": "Bearer xxxxx"
        }
      }
    }
  }
}
```

Dos modos de transporte soportados:

| Modo | Config | Ejemplo |
|------|--------|---------|
| **Stdio** | `command` + `args` | Proceso local vía `npx` / `uvx` |
| **HTTP** | `url` + `headers` (opcional) | Endpoint remoto (`https://mcp.ejemplo.com/sse`) |

Usa `toolTimeout` para anular el timeout por defecto de 30s por llamada para servidores lentos:

```json
{
  "tools": {
    "mcpServers": {
      "mi-servidor-lento": {
        "url": "https://ejemplo.com/mcp/",
        "toolTimeout": 120
      }
    }
  }
}
```

Usa `enabledTools` para registrar solo un subconjunto de herramientas de un servidor MCP:

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/ruta/al/dir"],
        "enabledTools": ["read_file", "mcp_filesystem_write_file"]
      }
    }
  }
}
```

`enabledTools` acepta tanto el nombre raw de la herramienta MCP (por ejemplo `read_file`) como el nombre wrapped de nanobot (por ejemplo `mcp_filesystem_write_file`).

- Omite `enabledTools`, o configúralo a `["*"]`, para registrar todas las herramientas.
- Configura `enabledTools` a `[]` para no registrar herramientas de ese servidor.
- Configura `enabledTools` a una lista no vacía de nombres para registrar solo ese subconjunto.

Las herramientas MCP se descubren y registran automáticamente al inicio. El LLM puede usarlas junto con las herramientas integradas — sin configuración adicional.

### Seguridad

> [!TIP]
> Para despliegues en producción, configura `"restrictToWorkspace": true` en tu config para aislar al agente.
> En `v0.1.4.post3` y anteriores, un `allowFrom` vacío permitía a todos los remitentes. Desde `v0.1.4.post4`, `allowFrom` vacío deniega todo acceso por defecto. Para permitir a todos los remitentes, configura `"allowFrom": ["*"]`.

| Opción | Por defecto | Descripción |
|--------|-------------|-------------|
| `tools.restrictToWorkspace` | `false` | Cuando es `true`, restringe **todas** las herramientas del agente (shell, lectura/escritura/edición de archivos, listado) al directorio workspace. Previene path traversal y acceso fuera de alcance. |
| `tools.exec.enable` | `true` | Cuando es `false`, la herramienta shell `exec` no se registra en absoluto. Usa esto para deshabilitar completamente la ejecución de comandos shell. |
| `tools.exec.pathAppend` | `""` | Directorios extra para agregar a `PATH` al ejecutar comandos shell (ej. `/usr/sbin` para `ufw`). |
| `channels.*.allowFrom` | `[]` (deniega todo) | Lista blanca de IDs de usuario. Vacío deniega todo; usa `["*"]` para permitir a todos. |

### Zona Horaria

El tiempo es contexto. El contexto debe ser preciso.

Por defecto, nanobot usa `UTC` para el contexto de tiempo en ejecución. Si quieres que el agente piense en tu hora local, configura `agents.defaults.timezone` con un [nombre de zona horaria IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) válido:

```json
{
  "agents": {
    "defaults": {
      "timezone": "America/Mexico_City"
    }
  }
}
```

Esto afecta las cadenas de tiempo de ejecución mostradas al modelo, como el contexto de ejecución y los prompts de heartbeat. También se convierte en la zona horaria por defecto para los schedules de cron cuando una expresión cron omite `tz`, y para tiempos `at` de una sola ejecución cuando el datetime ISO no tiene offset explícito.

Ejemplos comunes: `UTC`, `America/Mexico_City`, `America/Bogota`, `America/Argentina/Buenos_Aires`, `America/Santiago`, `America/Lima`, `Europe/Madrid`, `America/New_York`, `America/Los_Angeles`, `Europe/London`, `Europe/Berlin`, `Asia/Tokyo`, `Asia/Shanghai`, `Asia/Singapore`, `Australia/Sydney`.

> ¿Necesitas otra zona horaria? Consulta la [Base de Datos de Zonas Horarias IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) completa.

## 🧩 Múltiples Instancias

Ejecuta múltiples instancias de nanobot simultáneamente con configs y datos de ejecución separados. Usa `--config` como punto de entrada principal. Opcionalmente pasa `--workspace` durante `onboard` cuando quieras inicializar o actualizar el workspace guardado para una instancia específica.

### Inicio Rápido

Si quieres que cada instancia tenga su propio workspace dedicado desde el inicio, pasa tanto `--config` como `--workspace` durante el onboarding.

**Inicializar instancias:**

```bash
# Crear configs e instancias separadas con workspaces
nanobot onboard --config ~/.nanobot-telegram/config.json --workspace ~/.nanobot-telegram/workspace
nanobot onboard --config ~/.nanobot-discord/config.json --workspace ~/.nanobot-discord/workspace
nanobot onboard --config ~/.nanobot-feishu/config.json --workspace ~/.nanobot-feishu/workspace
```

**Configurar cada instancia:**

Edita `~/.nanobot-telegram/config.json`, `~/.nanobot-discord/config.json`, etc. con diferentes configuraciones de canal. El workspace que pasaste durante `onboard` se guarda en cada config como el workspace por defecto de esa instancia.

**Ejecutar instancias:**

```bash
# Instancia A - Bot de Telegram
nanobot gateway --config ~/.nanobot-telegram/config.json

# Instancia B - Bot de Discord
nanobot gateway --config ~/.nanobot-discord/config.json

# Instancia C - Bot de Feishu con puerto personalizado
nanobot gateway --config ~/.nanobot-feishu/config.json --port 18792
```

### Resolución de Rutas

Cuando usas `--config`, nanobot deriva su directorio de datos de ejecución de la ubicación del archivo de configuración. El workspace sigue viniendo de `agents.defaults.workspace` a menos que lo anules con `--workspace`.

Para abrir una sesión CLI contra una de estas instancias localmente:

```bash
nanobot agent -c ~/.nanobot-telegram/config.json -m "Hola desde la instancia de Telegram"
nanobot agent -c ~/.nanobot-discord/config.json -m "Hola desde la instancia de Discord"

# Override de workspace de una sola vez
nanobot agent -c ~/.nanobot-telegram/config.json -w /tmp/nanobot-telegram-test
```

> `nanobot agent` inicia un agente CLI local usando el workspace/config seleccionado. No se adjunta ni hace proxy a través de un proceso `nanobot gateway` ya en ejecución.

| Componente | Resuelto Desde | Ejemplo |
|------------|----------------|---------|
| **Config** | ruta `--config` | `~/.nanobot-A/config.json` |
| **Workspace** | `--workspace` o config | `~/.nanobot-A/workspace/` |
| **Cron Jobs** | directorio de config | `~/.nanobot-A/cron/` |
| **Media / estado de ejecución** | directorio de config | `~/.nanobot-A/media/` |

### Cómo Funciona

- `--config` selecciona qué archivo de configuración cargar
- Por defecto, el workspace viene de `agents.defaults.workspace` en esa config
- Si pasas `--workspace`, anula el workspace de la config

### Configuración Mínima

1. Copia tu config base en un nuevo directorio de instancia.
2. Configura un `agents.defaults.workspace` diferente para esa instancia.
3. Inicia la instancia con `--config`.

Ejemplo de config:

```json
{
  "agents": {
    "defaults": {
      "workspace": "~/.nanobot-telegram/workspace",
      "model": "anthropic/claude-sonnet-4-6"
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "TU_TOKEN_DE_BOT_TELEGRAM"
    }
  },
  "gateway": {
    "port": 18790
  }
}
```

### Casos de Uso Comunes

- Ejecutar bots separados para Telegram, Discord, Feishu y otras plataformas
- Mantener instancias de testing y producción aisladas
- Usar diferentes modelos o proveedores para diferentes equipos
- Servir múltiples tenants con configs y datos de ejecución separados

### Notas

- Cada instancia debe usar un puerto diferente si se ejecutan al mismo tiempo
- Usa un workspace diferente por instancia si quieres memoria, sesiones y skills aislados
- `--workspace` anula el workspace definido en la config
- Los cron jobs y estado de media/ejecución se derivan del directorio de configuración

## 💻 Referencia CLI

| Comando | Descripción |
|---------|-------------|
| `nanobot onboard` | Inicializar config y workspace en `~/.nanobot/` |
| `nanobot onboard --wizard` | Lanzar el asistente de configuración interactivo |
| `nanobot onboard -c <config> -w <workspace>` | Inicializar o refrescar una config de instancia específica |
| `nanobot agent -m "..."` | Chatear con el agente |
| `nanobot agent -w <workspace>` | Chatear contra un workspace específico |
| `nanobot agent -w <workspace> -c <config>` | Chatear contra un workspace/config específico |
| `nanobot agent` | Modo de chat interactivo |
| `nanobot agent --no-markdown` | Mostrar respuestas en texto plano |
| `nanobot agent --logs` | Mostrar logs de ejecución durante el chat |
| `nanobot serve` | Iniciar la API compatible con OpenAI |
| `nanobot gateway` | Iniciar el gateway |
| `nanobot status` | Mostrar estado |
| `nanobot provider login openai-codex` | Login OAuth para proveedores |
| `nanobot channels login <canal>` | Autenticar un canal interactivamente |
| `nanobot channels status` | Mostrar estado de canales |

Salir del modo interactivo: `exit`, `quit`, `/exit`, `/quit`, `:q`, o `Ctrl+D`.

<details>
<summary><b>Heartbeat (Tareas Periódicas)</b></summary>

El gateway se despierta cada 30 minutos y revisa `HEARTBEAT.md` en tu workspace (`~/.nanobot/workspace/HEARTBEAT.md`). Si el archivo tiene tareas, el agente las ejecuta y entrega resultados a tu canal de chat más recientemente activo.

**Configurar:** edita `~/.nanobot/workspace/HEARTBEAT.md` (creado automáticamente por `nanobot onboard`):

```markdown
## Tareas Periódicas

- [ ] Revisar pronóstico del clima y enviar resumen
- [ ] Escanear bandeja de entrada en busca de emails urgentes
```

El agente también puede gestionar este archivo él mismo — pídele que "agregue una tarea periódica" y actualizará `HEARTBEAT.md` por ti.

> **Nota:** El gateway debe estar ejecutándose (`nanobot gateway`) y debes haber chateado con el bot al menos una vez para que sepa a qué canal entregar.

</details>

## 🐍 SDK Python

Usa nanobot como librería — sin CLI, sin gateway, solo Python:

```python
from nanobot import Nanobot

bot = Nanobot.from_config()
result = await bot.run("Resume el README")
print(result.content)
```

Cada llamada lleva un `session_key` para aislamiento de conversación — diferentes keys obtienen historial independiente:

```python
await bot.run("hola", session_key="usuario-alice")
await bot.run("hola", session_key="tarea-42")
```

Agrega hooks de ciclo de vida para observar o personalizar al agente:

```python
from nanobot.agent import AgentHook, AgentHookContext

class AuditHook(AgentHook):
    async def before_execute_tools(self, ctx: AgentHookContext) -> None:
        for tc in ctx.tool_calls:
            print(f"[herramienta] {tc.name}")

result = await bot.run("Hola", hooks=[AuditHook()])
```

Consulta [docs/PYTHON_SDK.md](PYTHON_SDK.md) para la referencia completa del SDK.

## 🔌 API Compatible con OpenAI

nanobot puede exponer un endpoint mínimo compatible con OpenAI para integraciones locales:

```bash
pip install "nanobot-ai[api]"
nanobot serve
```

Por defecto, la API se vincula a `127.0.0.1:8900`. Puedes cambiar esto en `config.json`.

### Comportamiento

- Aislamiento de sesión: pasa `"session_id"` en el body de la solicitud para aislar conversaciones; omite para una sesión compartida por defecto (`api:default`)
- Entrada de mensaje único: cada solicitud debe contener exactamente un mensaje `user`
- Modelo fijo: omite `model`, o pasa el mismo modelo mostrado por `/v1/models`
- Sin streaming: `stream=true` no está soportado

### Endpoints

- `GET /health`
- `GET /v1/models`
- `POST /v1/chat/completions`

### curl

```bash
curl http://127.0.0.1:8900/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "hola"}],
    "session_id": "mi-sesion"
  }'
```

### Python (`requests`)

```python
import requests

resp = requests.post(
    "http://127.0.0.1:8900/v1/chat/completions",
    json={
        "messages": [{"role": "user", "content": "hola"}],
        "session_id": "mi-sesion",  # opcional: aislar conversación
    },
    timeout=120,
)
resp.raise_for_status()
print(resp.json()["choices"][0]["message"]["content"])
```

### Python (`openai`)

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8900/v1",
    api_key="dummy",
)

resp = client.chat.completions.create(
    model="MiniMax-M2.7",
    messages=[{"role": "user", "content": "hola"}],
    extra_body={"session_id": "mi-sesion"},  # opcional: aislar conversación
)
print(resp.choices[0].message.content)
```

## 🐳 Docker

> [!TIP]
> La bandera `-v ~/.nanobot:/root/.nanobot` monta tu directorio de config local dentro del contenedor, para que tu config y workspace persistan entre reinicios del contenedor.

### Docker Compose

```bash
docker compose run --rm nanobot-cli onboard   # configuración inicial
vim ~/.nanobot/config.json                     # agregar API keys
docker compose up -d nanobot-gateway           # iniciar gateway
```

```bash
docker compose run --rm nanobot-cli agent -m "¡Hola!"   # ejecutar CLI
docker compose logs -f nanobot-gateway                    # ver logs
docker compose down                                       # detener
```

### Docker

```bash
# Construir la imagen
docker build -t nanobot .

# Inicializar config (solo la primera vez)
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot onboard

# Editar config en el host para agregar API keys
vim ~/.nanobot/config.json

# Ejecutar gateway (se conecta a canales habilitados, ej. Telegram/Discord/Mochat)
docker run -v ~/.nanobot:/root/.nanobot -p 18790:18790 nanobot gateway

# O ejecutar un solo comando
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot agent -m "¡Hola!"
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot status
```

## 🐧 Servicio Linux

Ejecuta el gateway como servicio de systemd de usuario para que se inicie automáticamente y se reinicie en caso de fallo.

**1. Encontrar la ruta del binario de nanobot:**

```bash
which nanobot   # ej. /home/usuario/.local/bin/nanobot
```

**2. Crear el archivo de servicio** en `~/.config/systemd/user/nanobot-gateway.service` (reemplaza la ruta de `ExecStart` si es necesario):

```ini
[Unit]
Description=Nanobot Gateway
After=network.target

[Service]
Type=simple
ExecStart=%h/.local/bin/nanobot gateway
Restart=always
RestartSec=10
NoNewPrivileges=yes
ProtectSystem=strict
ReadWritePaths=%h

[Install]
WantedBy=default.target
```

**3. Habilitar e iniciar:**

```bash
systemctl --user daemon-reload
systemctl --user enable --now nanobot-gateway
```

**Operaciones comunes:**

```bash
systemctl --user status nanobot-gateway        # verificar estado
systemctl --user restart nanobot-gateway       # reiniciar después de cambios en config
journalctl --user -u nanobot-gateway -f        # seguir logs
```

Si editas el archivo `.service`, ejecuta `systemctl --user daemon-reload` antes de reiniciar.

> **Nota:** Los servicios de usuario solo se ejecutan mientras estás logueado. Para mantener el gateway corriendo después de cerrar sesión, habilita lingering:
>
> ```bash
> loginctl enable-linger $USER
> ```

## 📁 Estructura del Proyecto

```
nanobot/
├── agent/          # 🧠 Lógica central del agente
│   ├── loop.py     #    Loop del agente (LLM ↔ ejecución de herramientas)
│   ├── context.py  #    Constructor de prompts
│   ├── memory.py   #    Memoria persistente
│   ├── skills.py   #    Cargador de skills
│   ├── subagent.py #    Ejecución de tareas en segundo plano
│   └── tools/      #    Herramientas integradas (incl. spawn)
├── skills/         # 🎯 Skills incluidos (github, weather, tmux...)
├── channels/       # 📱 Integraciones de canales de chat (soporta plugins)
├── bus/            # 🚌 Enrutamiento de mensajes
├── cron/           # ⏰ Tareas programadas
├── heartbeat/      # 💓 Activación proactiva
├── providers/      # 🤖 Proveedores LLM (OpenRouter, etc.)
├── session/        # 💬 Sesiones de conversación
├── config/         # ⚙️ Configuración
└── cli/            # 🖥️ Comandos
```

## 🤝 Contribuir y Roadmap

¡Los PRs son bienvenidos! El código es intencionalmente pequeño y legible. 🤗

### Estrategia de Branches

| Branch | Propósito |
|--------|-----------|
| `main` | Releases estables — correcciones de bugs y mejoras menores |
| `nightly` | Funciones experimentales — nuevas funciones y cambios importantes |

**¿No estás seguro a qué branch apuntar?** Consulta [CONTRIBUTING.md](../CONTRIBUTING.md) para más detalles.

**Roadmap** — ¡Elige un elemento y [abre un PR](https://github.com/HKUDS/nanobot/pulls)!

- [ ] **Multi-modal** — Ver y escuchar (imágenes, voz, video)
- [ ] **Memoria a largo plazo** — Nunca olvidar contexto importante
- [ ] **Mejor razonamiento** — Planificación y reflexión de múltiples pasos
- [ ] **Más integraciones** — Calendario y más
- [ ] **Auto-mejora** — Aprender de retroalimentación y errores

### Contribuidores

<a href="https://github.com/HKUDS/nanobot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/nanobot&max=100&columns=12&updated=20260210" alt="Contribuidores" />
</a>

## ⭐ Historial de Estrellas

<div align="center">
  <a href="https://star-history.com/#HKUDS/nanobot&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" style="border-radius: 15px; box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);" />
    </picture>
  </a>
</div>

<p align="center">
  <em>¡Gracias por visitar ✨ nanobot!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.nanobot&style=for-the-badge&color=00d4ff" alt="Visitas">
</p>

<p align="center">
  <sub>nanobot es solo para fines educativos, de investigación e intercambio técnico</sub>
</p>
