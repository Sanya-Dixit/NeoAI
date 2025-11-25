param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('online','offline','test','menu')]
    [string]$Mode
)

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$python = Join-Path $repoRoot ".\.venv\Scripts\python.exe"

switch ($Mode) {
    'online' {
        Write-Host "Launching Online mode (main.py)"
        & $python (Join-Path $repoRoot 'main.py')
    }
    'offline' {
        Write-Host "Launching Offline mode (neo_offline.py)"
        & $python (Join-Path $repoRoot 'neo_offline.py')
    }
    'test' {
        Write-Host "Running quick_test.py"
        & $python (Join-Path $repoRoot 'quick_test.py')
    }
    'menu' {
        Write-Host "Opening menu (run_neo_menu.bat)"
        Start-Process -FilePath 'cmd.exe' -ArgumentList "/k run_neo_menu.bat" -WorkingDirectory $repoRoot
    }
}
