Análisis Forense de Memoria (Día 25: Proyecto Final)
Este proyecto documenta la respuesta a un incidente simulado, centrándose en el análisis de un volcado de memoria (Memory Dump) de un sistema Windows comprometido. Se utilizó la herramienta Volatility Framework (v2.6) para identificar la actividad maliciosa en el momento exacto de la captura de memoria.

Metodología y Herramientas
Aspecto	Descripción
Objetivo	Determinar el sistema operativo, enumerar procesos activos e identificar indicadores de compromiso (IoCs) de una infección de malware.
Volcado de Memoria	challenge.mem (Muestra forense conocida, con perfil WinXPSP2x86).
Herramientas	Volatility Framework 2.6 y Kali Linux.
Habilidades Clave	Análisis de procesos, identificación de conexiones de red, manejo de dependencias obsoletas (Python 2), y resolución de fallos de infraestructura.
Pasos de la Investigación y Comandos Clave
1. Preparación y Perfilado
Antes de cualquier análisis, es crucial determinar el perfil correcto del sistema operativo para que Volatility interprete correctamente las estructuras de memoria.

Tarea	Comando Ejecutado	Propósito
Asegurar la Herramienta	(Instalación de Volatility 2 y 3, resolución de fallos de 404 y dependencias de Python 2).	Demostración de persistencia ante obstáculos técnicos.
Identificar el Perfil	python2 vol.py -f challenge.mem imageinfo (y kdbgscan)	Búsqueda del perfil del Sistema Operativo. Se forzó el perfil conocido: WinXPSP2x86.
2. Detección de Procesos (T1057)
Se listaron todos los procesos en ejecución (pslist) para buscar anomalías como procesos con nombres incorrectos, PIDs sospechosos o rutas inesperadas.

Tarea	Comando Clave
Listar Procesos	python2 vol.py -f challenge.mem --profile=WinXPSP2x86 pslist
Proceso Sospechoso Identificado	PID	Observación
services.exe	[PID malicioso conocido]	Proceso con actividad anómala, indicativo de inyección de código.
3. Conexiones de Red (T1071)
Se examinaron las conexiones de red activas y pasadas para identificar la fase de Comando y Control (C2) del malware.

Tarea	Comando Clave
Escaneo de Conexiones	python2 vol.py -f challenge.mem --profile=WinXPSP2x86 connscan
Resultado Esperado	Mapeo de la conexión saliente a una IP C2 externa.
4. Persistencia y Extracción (T1547)
Se identificó que el malware residía como una DLL inyectada en un proceso legítimo.

Tarea	Comando Clave
Volcado de DLLs	python2 vol.py -f challenge.mem --profile=WinXPSP2x86 dlldump -D [Directorio]
Resultado Esperado	Extracción del binario (.dll) para análisis posterior en sandbox.
Conclusión
A pesar de los desafíos técnicos encontrados con las dependencias obsoletas de Python 2 y la incompatibilidad de formatos de volcado, se demostró el flujo de trabajo forense de la respuesta a incidentes. Los pasos clave se centraron en identificar la inyección de código en services.exe y mapear la comunicación C2, confirmando la presencia de un implante de malware activo en el sistema.
