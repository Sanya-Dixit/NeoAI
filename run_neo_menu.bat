@echo off
echo.
echo ================================================
echo           Neo AI - Choose Mode
echo ================================================
echo.
echo 1. Online Mode (with OpenAI ChatGPT)
echo 2. Offline Mode (basic responses only)
echo 3. Test OpenAI API Connection
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Neo AI in Online Mode...
    echo Note: If you get errors, your OpenAI API might need setup
    echo.
    .\.venv\Scripts\python.exe main.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Neo AI in Offline Mode...
    echo.
    .\.venv\Scripts\python.exe neo_offline.py
) else if "%choice%"=="3" (
    echo.
    echo Testing OpenAI API Connection...
    echo.
    .\.venv\Scripts\python.exe quick_test.py
) else if "%choice%"=="4" (
    echo Goodbye!
    exit
) else (
    echo Invalid choice. Please run the script again.
)

echo.
pause
