setenv CONDA_EXE "`cygpath 'X:/nsi/conda_install\Scripts\conda.exe'`";
setenv _CONDA_EXE "`cygpath 'X:/nsi/conda_install\Scripts\conda.exe'`";
unsetenv _CE_M;
unsetenv _CE_CONDA;
setenv CONDA_PYTHON_EXE "`cygpath 'X:/nsi/conda_install\python.exe'`";
setenv _CONDA_ROOT "`cygpath 'X:/nsi/conda_install'`";

source "`cygpath 'X:/nsi/conda_install\Lib\site-packages\conda\shell\etc\profile.d\conda.csh'`"