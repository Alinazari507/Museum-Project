#!/bin/bash
echo "🚀 Starting Workbench Setup..."

# 1. Python Setup
python3 -m venv .venv
source .venv/bin/activate
pip install PyYAML

# 2. TypeScript Setup
npm init -y
npm install --save-dev typescript
npx tsc --init

# 3. Git Setup
echo ".venv/
node_modules/
__pycache__/" > .gitignore

echo "✅ Setup Complete! Environment is ready."
