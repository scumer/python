@echo off

PyInstaller -y -F --icon icon\up.ico --distpath build --specpath build  --version-file src\version.txt -n THDataUP src\THDataUPWinSvc.py

echo.
pause