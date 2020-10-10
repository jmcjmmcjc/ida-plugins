@echo off

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system" 
 
if '%errorlevel%' NEQ '0' (  
    goto UACPrompt  
) else ( goto gotAdmin )  
   
:UACPrompt  
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs" 
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs" 
    "%temp%\getadmin.vbs" 
    exit /B  
   
:gotAdmin  
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )  
    pushd "%CD%" 
    CD /D "%~dp0" 
 
:begin

set IDA_PRO_USER_PLUGINS=%APPDATA%\Hex-Rays\IDA Pro\plugins
call :mk_soft_link auto_re
call :mk_soft_link hexrays_hlight
call :mk_soft_link batch_rename
call :mk_soft_link idajmc
pause

:mk_soft_link
del "%IDA_PRO_USER_PLUGINS%\%~1.py"
mklink "%IDA_PRO_USER_PLUGINS%\%~1.py" "%~dp0\%~1\%~1.py"
goto :eof
