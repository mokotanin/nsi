$Env:CONDA_EXE = "X:/nsi/conda_install\Scripts\conda.exe"
$Env:_CONDA_EXE = "X:/nsi/conda_install\Scripts\conda.exe"
$Env:_CE_M = $null
$Env:_CE_CONDA = $null
$Env:CONDA_PYTHON_EXE = "X:/nsi/conda_install\python.exe"
$Env:_CONDA_ROOT = "X:/nsi/conda_install"
$CondaModuleArgs = @{ChangePs1 = $True}

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs