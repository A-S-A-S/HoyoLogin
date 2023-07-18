$projectDirectory = $PSScriptRoot
$Users = @{}

# Generate tokens.json
while ($true) {
    $user = Read-Host "Enter custom name for user (optional)"
    $cookieValue = Read-Host "Open the site, execute the command `document.cookie` to retrieve the cookie value. Enter it here"

    $Users[$user] = $cookieValue

    $choice = Read-Host "Do you want to add another user? (Y/N, Default = No)"
    if ($choice.ToLower() -ne "y") {
        break
    }
}

$filePath = Join-Path $projectDirectory "tokens.json"
$Users | ConvertTo-Json | Set-Content -NoNewline -encoding ASCII $filePath

Write-Host "tokens.json file created successfully."

# Generate Login.bat
$loginBatContent = @"
@echo off
cd /d "$projectDirectory"
python main.py
pause
"@

$loginBatPath = Join-Path $projectDirectory "login.bat"
$loginBatContent | Out-File -Encoding ASCII $loginBatPath

Write-Host "login.bat file created successfully."

# Install requests
$choice = Read-Host "Do you have requests lib? (Y/N, Default = Yes)"
if ($choice.ToLower() -eq "n") {
    try {
        pip install requests
        Write-Host "Requirements installed successfully."
    }
    catch {
        Write-Host "Failed to install requirements. Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Schedule Task
$choice = Read-Host "Do you want to schedule the task? (Y/N, Default = No)"
if ($choice.ToLower() -eq "y") {
    $taskName = "HoyoLogin"
    $pythonExe = Get-Command python | Select-Object -ExpandProperty Path
    $scriptPath = Join-Path $projectDirectory "main.py"
    $taskAction = New-ScheduledTaskAction -Execute $pythonExe -Argument $scriptPath
    $taskTrigger = New-ScheduledTaskTrigger -Daily -At 21:00
    $taskSettings = New-ScheduledTaskSettingsSet

    try {
        Register-ScheduledTask -TaskName $taskName -Action $taskAction -Trigger $taskTrigger -Settings $taskSettings -User "NT AUTHORITY\SYSTEM"
        Write-Host "Task scheduled successfully at 21:00"
    }
    catch {
        Write-Host "Failed to schedule the task. Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}