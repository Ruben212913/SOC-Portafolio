# simulate_user_creation.ps1
# Este script simula el comando de creación de un usuario local y su adición a un grupo,
# tal como un atacante lo haría después de obtener acceso inicial (T1136.001).
# En un entorno real, estos comandos tendrían efecto en el sistema.
# Propósito: Demostrar conocimiento teórico de la técnica.

Write-Host "Simulando la creación del usuario 'tempuser' y añadiéndolo a 'Administrators'."
Write-Host "Comando 1: net user tempuser Password123! /add"
Write-Host "Comando 2: net localgroup administrators tempuser /add"
Write-Host "--------------------------------------------------------"
Write-Host "En un sistema Windows real, esto generaría Event IDs 4720 y 4732."
Write-Host "Busca Event ID 4720 (User Account Created) y 4732 (Member Added to Security-Enabled Local Group)."
