:: simulate_cmd_execution.cmd
:: Este script simula la ejecución de comandos básicos del sistema (T1059.003),
:: como los que un atacante usaría para reconocimiento.
:: Propósito: Demostrar conocimiento teórico de la técnica.

@echo off
echo Simulando la ejecucion del comando "whoami"
echo Comando: whoami
echo --------------------------------------------------------
echo En un sistema Windows real, esto generaria un Event ID 4688 (Process Creation).
echo Busca 'cmd.exe' en el New Process Name y 'whoami' en la Command Line.
