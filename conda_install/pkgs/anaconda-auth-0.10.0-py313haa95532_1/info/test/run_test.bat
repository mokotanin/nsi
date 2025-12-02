



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "from anaconda_auth import __version__; assert __version__ == '0.10.0'"
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
