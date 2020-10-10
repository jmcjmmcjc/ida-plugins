@echo off

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
