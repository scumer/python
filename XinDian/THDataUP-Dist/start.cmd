@echo off
cd /d %~dp0
THDataUP.exe --startup auto install && echo. && sc failure "THDataUP"  actions= restart/0/restart/0/restart/0 reset= 0 && echo. && THDataUP.exe start 
echo.
net start | findstr "THDataUP" > NUL 
if %errorlevel% equ 0 (echo 服务已经启动) else (echo 服务未启动)
::sc config "THDataUP"  start= auto 

echo.
pause