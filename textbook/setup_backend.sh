#!/bin/bash

echo "🚀 Starting Physical AI Textbook Project Setup..."
echo ""

# Backend setup
echo "📦 Setting up Backend (Python)..."
cd backend

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Backend setup complete!"
echo ""
echo "⚙️  Next steps:"
echo "1. Copy backend/.env.example to backend/.env"
echo "2. Fill in your API keys (Qdrant, Neon, OpenRouter)"
echo "3. Run: python database.py (to create tables)"
echo "4. Run: python embeddings.py (to embed documents)"
echo "5. Run: python main.py (to start the server)"
echo ""

cd ..

# Frontend setup
echo "🎨 Frontend setup will be done separately with npm install"
echo ""
echo "To start the frontend:"
echo "1. cd textbook"
echo "2. npm install"
echo "3. npm start"
echo ""
echo "🎉 Setup script complete!"
