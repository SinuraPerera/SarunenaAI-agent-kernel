#!/bin/bash

# SaruNena AI Build Script
# This script sets up the development environment for SaruNena AI

set -e

echo "🌱 Setting up SaruNena AI development environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install uv first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Install Agent Kernel dependencies
echo "📦 Installing Agent Kernel dependencies..."
cd ../../ak-py
./build.sh

# Install SaruNena dependencies
echo "📦 Installing SaruNena dependencies..."
cd ../use-cases/sarunena-ai
uv sync

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "🔧 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your API keys before running the application"
fi

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your API keys"
echo "2. Run: python app_kernel.py"
echo "3. Access the web interface at http://localhost:5000"
