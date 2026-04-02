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

⚡️ Ofrece funcionalidad completa de agente con **99% menos líneas de código** que OpenClaw.

> 🐈 nanobot es solo para fines educativos, de investigación e intercambio técnico.

## Características principales

🪶 **Ultra-Ligero**: Una implementación super ligera de OpenClaw — 99% más pequeña, significativamente más rápida.

🔬 **Listo para investigación**: Código limpio y legible, fácil de entender, modificar y extender.

⚡️ **Veloz**: Arranque rápido, bajo uso de recursos e iteraciones más rápidas.

💎 **Fácil de usar**: Un solo comando para desplegar y listo.

## 📦 Instalación

### Requisitos previos

- **Python 3.11** o superior
- **Git** (para instalación desde código fuente)

### Opción 1: Desde código fuente (recomendado para desarrollo)

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

### Opción 2: Con [uv](https://github.com/astral-sh/uv) (estable, rápido)

```bash
uv tool install nanobot-ai
```

### Opción 3: Desde PyPI (estable)

```bash
pip install nanobot-ai
```

### Actualizar a la última versión

```bash
# PyPI / pip
pip install -U nanobot-ai
nanobot --version

# uv
uv tool upgrade nanobot-ai
nanobot --version
```

## 🚀 Inicio rápido

### 1. Inicializar

```bash
nanobot onboard
```

Usa `nanobot onboard --wizard` para el asistente de configuración interactivo.

### 2. Configurar (`~/.nanobot/config.json`)

Configura estas **dos partes** (las demás opciones tienen valores por defecto).

*Tu clave API* (ej. OpenRouter, recomendado):
```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  }
}
```

*Tu modelo*:
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

### 3. Chatear

```bash
nanobot agent
```

¡Eso es todo! Tienes un asistente de IA funcionando en 2 minutos.

## 💬 Conectar con apps de chat

Conecta nanobot a tu plataforma favorita:

| Canal | Lo que necesitas |
|-------|-----------------|
| **Telegram** | Token de bot de @BotFather |
| **Discord** | Token de bot + Message Content intent |
| **WhatsApp** | Escaneo de QR (`nanobot channels login whatsapp`) |
| **WeChat** | Escaneo de QR (`nanobot channels login weixin`) |
| **Feishu** | App ID + App Secret |
| **DingTalk** | App Key + App Secret |
| **Slack** | Bot token + App-Level token |
| **Matrix** | URL del homeserver + Access token |
| **Email** | Credenciales IMAP/SMTP |

### Ejemplo: Telegram (Recomendado)

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
      "allowFrom": ["TU_ID_DE_USUARIO"]
    }
  }
}
```

> Puedes encontrar tu **User ID** en la configuración de Telegram. Cópialo **sin el símbolo `@`**.

**3. Ejecutar**

```bash
nanobot gateway
```

Para configuración detallada de otros canales, consulta el [README principal](../README.md#-chat-apps).

## ⚙️ Configuración

Archivo de configuración: `~/.nanobot/config.json`

### Proveedores de LLM

| Proveedor | Propósito | Obtener API Key |
|-----------|-----------|----------------|
| `openrouter` | LLM (recomendado, acceso a todos los modelos) | [openrouter.ai](https://openrouter.ai) |
| `anthropic` | LLM (Claude directo) | [console.anthropic.com](https://console.anthropic.com) |
| `openai` | LLM (GPT directo) | [platform.openai.com](https://platform.openai.com) |
| `deepseek` | LLM (DeepSeek directo) | [platform.deepseek.com](https://platform.deepseek.com) |
| `groq` | LLM + **Transcripción de voz** (Whisper) | [console.groq.com](https://console.groq.com) |
| `gemini` | LLM (Gemini directo) | [aistudio.google.com](https://aistudio.google.com) |
| `ollama` | LLM (local) | — |
| `custom` | Cualquier endpoint compatible con OpenAI | — |

> Para la lista completa de proveedores, consulta el [README principal](../README.md#providers).

### Búsqueda web

nanobot soporta múltiples proveedores de búsqueda web:

| Proveedor | Gratis |
|-----------|--------|
| `duckduckgo` | Sí (sin configuración) |
| `brave` (por defecto) | No |
| `tavily` | No |
| `jina` | Sí (nivel gratuito de 10M tokens) |
| `searxng` | Sí (auto-hospedado) |

Cuando no hay credenciales configuradas, nanobot automáticamente usa DuckDuckGo.

### MCP (Model Context Protocol)

nanobot soporta [MCP](https://modelcontextprotocol.io/) — conecta servidores de herramientas externos:

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

> El formato de configuración es compatible con Claude Desktop / Cursor.

### Zona horaria

Por defecto, nanobot usa `UTC`. Para usar tu hora local:

```json
{
  "agents": {
    "defaults": {
      "timezone": "America/Mexico_City"
    }
  }
}
```

Ejemplos comunes: `America/Mexico_City`, `America/Bogota`, `America/Argentina/Buenos_Aires`, `America/Santiago`, `Europe/Madrid`, `America/Lima`.

### Seguridad

| Opción | Por defecto | Descripción |
|--------|-------------|-------------|
| `tools.restrictToWorkspace` | `false` | Restringe las herramientas del agente al directorio workspace |
| `tools.exec.enable` | `true` | Habilita/deshabilita la ejecución de comandos shell |
| `channels.*.allowFrom` | `[]` (deniega todo) | Lista blanca de IDs de usuario. Usa `["*"]` para permitir a todos |

## 💻 Referencia CLI

| Comando | Descripción |
|---------|-------------|
| `nanobot onboard` | Inicializar configuración y workspace |
| `nanobot onboard --wizard` | Asistente de configuración interactivo |
| `nanobot agent` | Modo de chat interactivo |
| `nanobot agent -m "..."` | Enviar un mensaje al agente |
| `nanobot gateway` | Iniciar el gateway (para canales de chat) |
| `nanobot status` | Mostrar estado |
| `nanobot channels login <canal>` | Autenticar un canal |

## 🐳 Docker

```bash
# Construir la imagen
docker build -t nanobot .

# Inicializar (solo la primera vez)
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot onboard

# Editar config para agregar API keys
vim ~/.nanobot/config.json

# Ejecutar gateway
docker run -v ~/.nanobot:/root/.nanobot -p 18790:18790 nanobot gateway

# O enviar un mensaje
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot agent -m "¡Hola!"
```

## 🐧 Servicio en Linux

Ejecuta el gateway como servicio de systemd para que se inicie automáticamente:

```bash
# Crear archivo de servicio en ~/.config/systemd/user/nanobot-gateway.service
# Ver README principal para el contenido completo

systemctl --user daemon-reload
systemctl --user enable --now nanobot-gateway

# Verificar estado
systemctl --user status nanobot-gateway
```

## 🤝 Contribuir

¡Los PRs son bienvenidos! El código es intencionalmente pequeño y legible. 🤗

| Branch | Propósito |
|--------|-----------|
| `main` | Releases estables — correcciones y mejoras menores |
| `nightly` | Funciones experimentales — nuevas funciones y cambios importantes |

Consulta [CONTRIBUTING.md](../CONTRIBUTING.md) para más detalles.

## 📚 Más información

Para documentación completa incluyendo todas las opciones de configuración, múltiples instancias, SDK de Python, API compatible con OpenAI y más, consulta el [README principal en inglés](../README.md).

---

<p align="center">
  <sub>nanobot es solo para fines educativos, de investigación e intercambio técnico.</sub>
</p>
