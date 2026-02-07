#!/bin/bash
set -e

CONFIG_DIR="/root/.nanobot"
CONFIG_FILE="$CONFIG_DIR/config.json"

# Create config directory if it doesn't exist
mkdir -p "$CONFIG_DIR"

# Only create config if it doesn't exist (persistence!)
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Creating nanobot config from environment variables..."
    
    cat > "$CONFIG_FILE" << EOF
{
  "providers": {
    "openrouter": {
      "apiKey": "${OPENROUTER_KEY}"
    }
  },
  "telegram": {
    "token": "${TELEGRAM_TOKEN}",
    "allowedUsers": [${TELEGRAM_USER_ID}]
  },
  "defaultProvider": "openrouter",
  "defaultModel": "google/gemini-2.0-flash-exp:free"
}
EOF
    
    echo "✓ Config created at $CONFIG_FILE"
else
    echo "✓ Config already exists at $CONFIG_FILE (using persisted version)"
fi

# Show config for debugging (without sensitive data)
echo "Current config structure:"
cat "$CONFIG_FILE" | grep -v "apiKey\|token" || true

# Execute the command passed as arguments
echo "Starting: $@"
exec "$@"
