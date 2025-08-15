# Detección de Ataque de Reconocimiento de Red

## Propósito del Proyecto
Este proyecto demuestra cómo un **Analista SOC** puede detectar un ataque de reconocimiento de red (escaneo de puertos) usando los logs del firewall.

## Herramientas Utilizadas
- **Máquina del atacante:** Kali Linux (IP: 192.168.1.10)
- **Máquina de la víctima:** Ubuntu (IP: 192.168.1.20)
- **Comando de ataque:** `nmap -Pn 192.168.1.20`
- **Fuente de evidencia:** Archivo de log del firewall (`/var/log/ufw.log`)

## Evidencia del Ataque
A continuación se muestra la salida del log del firewall de Ubuntu, donde se registran los intentos de conexión de Nmap bloqueados.

2025-08-13T20:04:44.584036-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=53 ID=25776 PROTO=TCP SPT=34417 DPT=1723 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584059-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=45 ID=52767 PROTO=TCP SPT=34417 DPT=143 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584061-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=48 ID=32058 PROTO=TCP SPT=34417 DPT=8080 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584062-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=51 ID=24236 PROTO=TCP SPT=34417 DPT=110 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584063-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=42 ID=47182 PROTO=TCP SPT=34417 DPT=80 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584070-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=44 ID=4580 PROTO=TCP SPT=34417 DPT=22 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584102-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=37 ID=27188 PROTO=TCP SPT=34417 DPT=5900 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:44.584103-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=51 ID=7712 PROTO=TCP SPT=34417 DPT=53 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:45.691003-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=54 ID=53005 PROTO=TCP SPT=34419 DPT=53 WINDOW=1024 RES=0x00 SYN URGP=0
2025-08-13T20:04:45.691054-06:00 ren-VirtualBox kernel: [UFW BLOCK] IN=enp0s3 OUT= MAC=08:00:27:6a:7d:d9:08:00:27:d1:f8:5d:08:00 SRC=192.168.1.10 DST=192.168.1.20 LEN=44 TOS=0x00 PREC=0x00 TTL=54 ID=29599 PROTO=TCP SPT=34419 DPT=5900 WINDOW=1024 RES=0x00 SYN URGP=0

## Análisis del Incidente (Español)
Las entradas del log muestran múltiples líneas con la etiqueta `[UFW BLOCK]` provenientes de la dirección IP 192.168.1.10. Esto indica que un escaneo de puertos fue bloqueado por el firewall. Esta evidencia es crucial para que un Analista SOC identifique un intento de reconocimiento y tome acciones defensivas.

## Incident Analysis (English)
The log entries show multiple lines with the `[UFW BLOCK]` tag coming from the IP address 192.168.1.10. This indicates that a port scan was blocked by the firewall. This evidence is crucial for a SOC Analyst to identify a reconnaissance attempt and take defensive actions.

