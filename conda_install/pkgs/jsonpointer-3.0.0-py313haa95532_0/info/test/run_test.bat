



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "from importlib.metadata import version; assert(version('jsonpointer')=='3.0.0')"
IF %ERRORLEVEL% NEQ 0 exit /B 1
pytest -vv tests.py
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
