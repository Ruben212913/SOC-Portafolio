# get_powershell_execution_logs.ps1
# Este script simula la busqueda de eventos de ejecucion de PowerShell.
# En un entorno real, 'Get-WinEvent' consultaria logs de Seguridad o PowerShell.
# Event ID 4688: A new process has been created (si se audita la linea de comandos).
# Event ID 4104: Script Block Logging (si esta habilitado el logging de PowerShell).
# Propósito: Demostrar conocimiento teórico de la busqueda de IOCs de uso de interpretes de comandos.

Write-Host "Simulando busqueda de ejecuciones de PowerShell y sus comandos..."
Write-Host "Comando 1 (Process Creation): Get-WinEvent -LogName Security -FilterXPath '*[System[(EventID=4688)]] and *[EventData[Data[@Name='NewProcessName'] and (Data='*powershell.exe*')]]'"
Write-Host "Comando 2 (Script Block Logging): Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -FilterXPath '*[System[(EventID=4104)]]'"
Write-Host "--------------------------------------------------------"
Write-Host "En un sistema Windows real, esto mostraria las lineas de comando ejecutadas o los bloques de script."
