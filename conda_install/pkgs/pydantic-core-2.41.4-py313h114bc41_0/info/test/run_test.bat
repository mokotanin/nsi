



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "from pydantic_core import PydanticUndefinedType"
IF %ERRORLEVEL% NEQ 0 exit /B 1
pytest -v --ignore=tests/test_docstrings.py --ignore=tests/test_hypothesis.py --ignore=tests/validators/test_allow_partial.py --ignore=tests/validators/test_frozenset.py --ignore=tests/validators/test_list.py --ignore=tests/validators/test_set.py
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
