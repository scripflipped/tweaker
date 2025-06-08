@echo off
echo Gaming PC Optimizer - Tweaker AIO
echo ================================
echo.
echo Checking for administrator privileges...

:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Administrator privileges confirmed.
    echo Starting Gaming PC Optimizer...
    echo.
    python main.py
) else (
    echo.
    echo ERROR: Administrator privileges required!
    echo Please right-click this file and select "Run as administrator"
    echo.
    pause
)

pause 