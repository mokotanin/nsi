



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "from importlib.metadata import version; assert(version('more-itertools')=='10.8.0')"
IF %ERRORLEVEL% NEQ 0 exit /B 1
pytest -v tests
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
