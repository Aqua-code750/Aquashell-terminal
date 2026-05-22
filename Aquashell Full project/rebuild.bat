@echo off
echo Cleaning old builds...
rmdir /s /q build
rmdir /s /q dist

echo Rebuilding AquaShell.exe...
python -m PyInstaller --onefile --icon=aquashell.ico --add-data "aquashell.ico;." aquashell.py

echo Build complete. Launching AquaShell.exe...
cd dist
AquaShell.exe
pause
