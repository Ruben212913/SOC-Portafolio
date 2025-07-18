# get_user_creation_events.ps1
# Este script simula la busqueda de eventos de creacion de usuarios en el log de Seguridad de Windows.
# En un entorno real, 'Get-WinEvent' consultaria el Visor de Eventos.
# Event ID 4720: User Account was Created.
# Event ID 4722: A user account was enabled.
# Event ID 4732: A member was added to a security-enabled local group (e.g., Administrators).
# Propósito: Demostrar conocimiento teórico de la busqueda de IOCs de acceso inicial.

Write-Host "Simulando busqueda de eventos de creacion de usuarios y adicion a grupos..."
Write-Host "Comando: Get-WinEvent -LogName Security -FilterXPath '*[System[(EventID=4720 or EventID=4722 or EventID=4732)]]'"
Write-Host "--------------------------------------------------------"
Write-Host "En un sistema Windows real, esto mostraria los detalles de los eventos encontrados."
Write-Host "Se buscaria por Source: 'Microsoft-Windows-Security-Auditing' y detalles de las nuevas cuentas."
