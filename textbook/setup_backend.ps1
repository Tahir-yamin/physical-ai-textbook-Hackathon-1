# Physical AI Textbook Setup Script for Windows

Write-Host "🚀 Starting Physical AI Textbook Project Setup..." -ForegroundColor Green
Write-Host ""

# Backend setup
Write-Host "📦 Setting up Backend (Python)..." -ForegroundColor Cyan
Set-Location backend

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "✅ Backend setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "⚙️  Next steps:" -ForegroundColor Cyan
Write-Host "1. Copy backend\.env.example to backend\.env"
Write-Host "2. Fill in your API keys (Qdrant, Neon, OpenRouter)"
Write-Host "3. Run: python database.py (to create tables)"
Write-Host "4. Run: python embeddings.py (to embed documents)"
Write-Host "5. Run: python main.py (to start the server)"
Write-Host ""

Set-Location ..

# Frontend info
Write-Host "🎨 Frontend setup" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the frontend:"
Write-Host "1. npm install"
Write-Host "2. npm start"
Write-Host ""
Write-Host "🎉 Setup script complete!" -ForegroundColor Green
