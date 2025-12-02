



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
pytest -v tests --ignore=tests/test_docs.py
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
