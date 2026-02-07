#!/bin/sh
set -e

# Create config.json from environment variables at runtime
cat > /root/.nanobot/config.json <<EOF
{
  "providers": {
    "openrouter": {
      "apiKey": "${OPENROUTER_KEY}"
    }
  },
  "agents": {
    "defaults": {
      "model": "google/gemini-3-flash-preview"
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "${TELEGRAM_TOKEN}",
      "allowFrom": ["${TELEGRAM_USER_ID}"]
    }
  }
}
EOF

# Execute the command passed to the container
exec "$@"
