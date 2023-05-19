$taskName = "HoyoLogin"
$action = New-ScheduledTaskAction -Execute 'C:\HoyoLogin\login.bat'
$trigger = New-ScheduledTaskTrigger -Daily -At 21:00
$settings = New-ScheduledTaskSettingsSet
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings
