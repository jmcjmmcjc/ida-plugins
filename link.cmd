set IDA_PRO_USER_PLUGINS=%APPDATA%\Hex-Rays\IDA Pro\plugins
set IDA_PLG_NAME=auto_re
del "%IDA_PRO_USER_PLUGINS%\%IDA_PLG_NAME%.py"
mklink "%IDA_PRO_USER_PLUGINS%\%IDA_PLG_NAME%.py" "%~dp0\%IDA_PLG_NAME%\%IDA_PLG_NAME%.py"
set IDA_PLG_NAME=hexrays_hlight
del "%IDA_PRO_USER_PLUGINS%\%IDA_PLG_NAME%.py"
mklink "%IDA_PRO_USER_PLUGINS%\%IDA_PLG_NAME%.py" "%~dp0\%IDA_PLG_NAME%\%IDA_PLG_NAME%.py"

set IDA_PLG_NAME=batch_rename
del "%IDA_PRO_USER_PLUGINS%\%IDA_PLG_NAME%.py"
mklink "%IDA_PRO_USER_PLUGINS%\%IDA_PLG_NAME%.py" "%~dp0\%IDA_PLG_NAME%\%IDA_PLG_NAME%.py"

pause
