@echo off
REM Linus Stores App - Setup Script for Windows
REM This script sets up the entire project

echo.
echo ================================
echo Linus Stores App - Setup Script
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    exit /b 1
)

echo [1/5] Checking Python installation...
python --version

echo.
echo [2/5] Setting up Backend...
cd backend

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing backend dependencies...
pip install -q -r requirements.txt

echo Backend setup complete!

echo.
echo [3/5] Creating .env file...
if not exist .env (
    copy .env.example .env
    echo Created .env file - Please edit with your MySQL credentials
) else (
    echo .env file already exists
)

cd ..

echo.
echo [4/5] Setting up Frontend...
cd frontend

echo Installing frontend dependencies...
pip install -q flask flask-cors

echo Frontend setup complete!

cd ..

echo.
echo [5/5] Setup Summary
echo ====================
echo.
echo ✓ Backend configured
echo ✓ Frontend configured  
echo ✓ Dependencies installed
echo.
echo Next steps:
echo 1. Edit backend\.env with your MySQL credentials
echo 2. Create database: mysql -u root -p ^< database\schema.sql
echo 3. Start Backend: cd backend ^& venv\Scripts\activate ^& python run.py
echo 4. Start Frontend (new terminal): cd frontend ^& python app.py
echo.
echo Then open: http://localhost:5001
echo.
pause
