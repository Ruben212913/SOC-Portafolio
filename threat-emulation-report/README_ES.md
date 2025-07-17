# Informe de Emulación de Amenazas - Red Team Atomic (Proyecto Compensatorio)

Este repositorio contiene la documentación relacionada con un ejercicio de emulación de amenazas, realizado como proyecto compensatorio para un curso avanzado de ciberseguridad. El objetivo principal de este proyecto fue simular tácticas específicas de adversarios utilizando los marcos de **Atomic Red Team** y luego llevar a cabo una **cacería de amenazas (threat hunting)** para detectar la evidencia de estas actividades dentro de un entorno Windows.

## Resumen del Proyecto

Este proyecto se centra en la aplicación práctica de las tácticas de **MITRE ATT&CK®**, específicamente:

* **TA0001 - Acceso Inicial (Initial Access)**: Explorando métodos que un adversario podría usar para obtener una entrada inicial en un sistema.
* **T1059 - Intérprete de Comandos y Scripts (Command and Scripting Interpreter)**: Simulando la ejecución de comandos y scripts por parte de un atacante con diversos propósitos maliciosos.
* **T1566 - Phishing**: Emulando un intento de phishing como un vector común de acceso inicial para comprometer credenciales de usuario o activar la ejecución de malware.

El segundo componente central de este proyecto implica la **cacería de amenazas**. Utilizando **PowerShell** para consultas activas y el **Visor de Eventos de Windows (Registros de Eventos)** para el análisis forense, esta sección detalla el proceso de búsqueda de indicadores de compromiso (IOCs) dejados por los ataques simulados.

## Herramientas y Tecnologías

Las siguientes herramientas y tecnologías clave fueron utilizadas a lo largo de este proyecto:

* **Atomic Red Team**: Utilizado para ejecutar pruebas predefinidas de emulación de adversarios que se mapean a las tácticas de MITRE ATT&CK.
* **PowerShell**: Empleado tanto para la ejecución de comandos maliciosos durante la fase de emulación como para realizar consultas exhaustivas de cacería de amenazas en el sistema.
* **Visor de Eventos de Windows (Registros de Eventos)**: Crucial para analizar la actividad del sistema, identificar eventos de seguridad y correlacionar registros para detectar evidencia de los ataques simulados.

## Estructura del Repositorio y Navegación

Este repositorio está organizado para proporcionar una visión clara del proyecto de emulación de amenazas. Aquí te presentamos un desglose de sus directorios clave y su contenido:

* **`README.md` / `README_ES.md`**: Estos archivos sirven como los puntos de entrada principales, proporcionando un resumen del proyecto en inglés y español, respectivamente.
* **`docs/`**: Contiene documentación suplementaria, como planes de ataque o definiciones de escenarios, relevantes para la configuración y ejecución del proyecto.
* **`informe/`**: Alberga el informe principal del proyecto (`informe_final.md`), que detalla las tácticas simuladas, la metodología de cacería de amenazas, los hallazgos y las conclusiones. Este directorio también incluye la subcarpeta `anexos/`, donde se almacenan todos los registros brutos (salidas de PowerShell, exportaciones del Visor de Eventos) y capturas de pantalla como evidencia.
* **`scripts/`**: Contiene todos los scripts de PowerShell utilizados durante el proyecto. Esto se clasifica adicionalmente en:
    * **`atomic_red_team/`**: Scripts utilizados específicamente para emular tácticas
