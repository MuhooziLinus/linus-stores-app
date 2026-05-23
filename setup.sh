#!/bin/bash
# Linus Stores App - Setup Script for macOS/Linux
# This script sets up the entire project

echo ""
echo "================================"
echo "Linus Stores App - Setup Script"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[1/5] Checking Python installation..."
python3 --version

echo ""
echo "[2/5] Setting up Backend..."
cd backend

if [ ! -d venv ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing backend dependencies..."
pip install -q -r requirements.txt

echo "Backend setup complete!"

echo ""
echo "[3/5] Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file - Please edit with your MySQL credentials"
else
    echo ".env file already exists"
fi

cd ..

echo ""
echo "[4/5] Setting up Frontend..."
cd frontend

echo "Installing frontend dependencies..."
pip install -q flask flask-cors

echo "Frontend setup complete!"

cd ..

echo ""
echo "[5/5] Setup Summary"
echo "===================="
echo ""
echo "✓ Backend configured"
echo "✓ Frontend configured"
echo "✓ Dependencies installed"
echo ""
echo "Next steps:"
echo "1. Edit backend/.env with your MySQL credentials"
echo "2. Create database: mysql -u root -p < database/schema.sql"
echo "3. Start Backend: cd backend && source venv/bin/activate && python run.py"
echo "4. Start Frontend (new terminal): cd frontend && python app.py"
echo ""
echo "Then open: http://localhost:5001"
echo ""
