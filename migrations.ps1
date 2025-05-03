# Path to your backend folder
$backendDir = Join-Path $PSScriptRoot 'backend'

# 1) Delete the migrations folder if it exists
$migrationsPath = Join-Path $backendDir 'migrations'
if (Test-Path $migrationsPath) {
    Write-Output "Deleting migrations folder..."
    Remove-Item $migrationsPath -Recurse -Force
} else {
    Write-Output "Migrations folder not found."
}

# 2) Delete __pycache__ folder in backend/app if it exists
$pycachePath = Join-Path $backendDir 'app\__pycache__'
if (Test-Path $pycachePath) {
    Write-Output "Deleting __pycache__ folder..."
    Remove-Item $pycachePath -Recurse -Force
} else {
    Write-Output "__pycache__ folder not found."
}

# 3) Activate the virtual environment
Write-Output "Activating virtual environment..."
& (Join-Path $PSScriptRoot 'venv\Scripts\Activate.ps1')

# 4) Change directory to the backend folder where run.py is located
Push-Location $backendDir

# 5) Set FLASK_APP to run.py (adjust if run.py is elsewhere)
$env:FLASK_APP = 'server.py'
$env:FLASK_ENV = 'development'

# 6) Run Flask-Migrate commands
Write-Output "Initializing migrations..."
flask db init

Write-Output "Generating migration script..."
flask db migrate -m "Initial migration"

Write-Output "Applying migrations..."
flask db upgrade

# Return to original directory
Pop-Location

Write-Output "✅ Migrations reset complete."
