



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "from importlib.metadata import version; assert(version('tomli')=='2.2.1')"
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
