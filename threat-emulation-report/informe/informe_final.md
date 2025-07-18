# Informe de Emulación y Cacería de Amenazas

## 1. Introducción

Este informe documenta un ejercicio de emulación y cacería de amenazas (threat hunting) realizado como proyecto compensatorio para un curso avanzado de ciberseguridad. El objetivo primordial fue aplicar conocimientos teóricos en un escenario práctico, simulando tácticas de adversarios del mundo real y desarrollando habilidades para su detección.

El ejercicio se centró en la emulación de tácticas específicas del marco **MITRE ATT&CK®**, incluyendo **Acceso Inicial (TA0001)**, el uso del **Intérprete de Comandos y Scripts (T1059)**, y la táctica de **Phishing (T1566)** como vector de entrada. Tras la simulación de estas actividades ofensivas, se conceptualizó una fase activa de cacería de amenazas, utilizando herramientas como **PowerShell** y el **Visor de Eventos de Windows**, para identificar y analizar la evidencia esperada de las acciones emuladas.

El propósito de este informe es detallar la metodología teórica empleada, los procedimientos de simulación, las técnicas de cacería aplicadas y los hallazgos anticipados, demostrando así la capacidad de comprender, simular y detectar actividades maliciosas en un entorno de red.

---

## 2. Metodología de Emulación de Amenazas

La fase de emulación de amenazas de este proyecto se diseñó para entender conceptualmente el comportamiento de un adversario real, utilizando técnicas y herramientas que se alinean con el marco MITRE ATT&CK®. El objetivo fue documentar el conocimiento teórico sobre cómo se replicarían estas acciones específicas para generar artefactos detectables en un entorno Windows. Para esto, se analizó el uso principal de **Atomic Red Team**, una librería de pruebas que permite ejecutar pequeñas y controladas simulaciones de tácticas de ataque.

Cada táctica fue investigada desde una perspectiva teórica, comprendiendo cómo sería su ejecución en un entorno de laboratorio controlado (una máquina virtual Windows vulnerable), los comandos involucrados y los eventos que se esperarían generar para su posterior detección.

### 2.1. Táctica: TA0001 - Acceso Inicial (Initial Access)

#### 2.1.1. Descripción de la Táctica
La táctica de Acceso Inicial representa los vectores que los adversarios utilizan para obtener su punto de apoyo inicial en una red o sistema. Esto puede incluir el uso de credenciales robadas, explotación de vulnerabilidades externas o la entrega de malware a través de phishing. Para este ejercicio, se analizó cómo se simularían escenarios comunes de compromiso inicial que dejarían una huella digital.

#### 2.1.2. Procedimiento de Simulación (Análisis Teórico)
Desde un punto de vista teórico, para simular el Acceso Inicial, se comprenderían las siguientes acciones controladas, utilizando Atomic Red Team (o scripts personalizados de PowerShell) para replicar comportamientos típicos de un atacante después de obtener acceso inicial:

* **Creación de Usuario Local (T1136.001 - Create Account: Local Account):** Se investigó la simulación de la creación de una cuenta de usuario local privilegiada. Esto representa un paso común de los adversarios para establecer persistencia una vez dentro.
    * **Comando/Técnica Específica Esperada:** `net user [nombre_usuario] [contraseña] /add` y `net localgroup administrators [nombre_usuario] /add`.
    * **Atomic Test ID (si aplica):** T1136.001 (ej. Atomic Test #1 - Create Local User).
    * **Propósito:** Comprender la detección de la creación de cuentas no autorizadas en logs de seguridad.
    * **Resultados Esperados:** La creación de un nuevo usuario y su adición a un grupo privilegiado generaría eventos específicos en el Visor de Eventos de Windows (ej., Event ID 4720 para creación de usuario, Event ID 4732 para adición a grupo de seguridad local).

* **Habilitación de Servicios Remotos (ej. WinRM, RDP):** Se analizó la emulación de la modificación de configuraciones de servicios para permitir el acceso remoto, una acción post-explotación común para facilitar el movimiento lateral o la persistencia.
    * **Comando/Técnica Específica Esperada:** Comandos de PowerShell para habilitar WinRM (`winrm quickconfig`) o RDP.
    * **Atomic Test ID (si aplica):** Atomic Red Team puede ofrecer tests como T1021.001 (RDP) o T1021.006 (WinRM).
    * **Propósito:** Entender cómo se identificaría la activación sospechosa de servicios de acceso remoto en los logs del sistema.
    * **Resultados Esperados:** La modificación de la configuración de servicios generaría eventos en los logs del sistema, indicando cambios en la configuración de firewall o el inicio de servicios.

### 2.2. Táctica: T1059 - Intérprete de Comandos y Scripts (Command and Scripting Interpreter)

#### 2.2.1. Descripción de la Táctica
La táctica de Intérprete de Comandos y Scripts implica el uso de interfaces de línea de comandos (CLI) o lenguajes de scripting (como PowerShell, Bash, Python) para ejecutar comandos que pueden manipular sistemas, descargar y ejecutar payloads, o interactuar con el sistema operativo de diversas maneras maliciosas. Esta táctica es fundamental para la mayoría de los adversarios, ya que les permite operar directamente sobre el sistema comprometido.

#### 2.2.2. Procedimiento de Simulación (Análisis Teórico)
Para comprender la emulación del uso de intérpretes de comandos y scripts, se investigó cómo se ejecutarían Atomic Tests que simulan cómo un atacante podría usar PowerShell o la línea de comandos para realizar acciones post-explotación:

* **Ejecución de Comandos con PowerShell (T1059.001 - PowerShell):** Se analizó la simulación de la ejecución de comandos PowerShell ofuscados o codificados. Esto representa el uso común de PowerShell por parte de los adversarios para reconocimiento, persistencia o movimiento lateral.
    * **Comando/Técnica Específica Esperada:** Ejemplos incluyen `powershell.exe -EncodedCommand ...` o el uso de `Invoke-AtomicTest T1059.001` para escenarios específicos.
    * **Atomic Test ID (si aplica):** T1059.001 (ej. Atomic Test #2 - PowerShell Remote Command Execution).
    * **Propósito:** Comprender la detección de la ejecución de PowerShell y comandos sospechosos mediante el monitoreo de procesos y argumentos de línea de comandos.
    * **Resultados Esperados:** La ejecución de PowerShell generaría eventos en los logs de seguridad (ej. Event ID 4688 con detalles de línea de comandos si el auditing está activado, o logs de PowerShell Script Block Logging).

* **Ejecución de Comandos del Sistema (T1059.003 - Cmd):** Se investigó la emulación de la ejecución de comandos `cmd.exe` que los adversarios utilizan para tareas como la enumeración de red, la manipulación de archivos o la interacción con el sistema.
    * **Comando/Técnica Específica Esperada:** Ejemplos incluyen `cmd.exe /c "whoami & ipconfig"` o el uso de `Invoke-AtomicTest T1059.003` para comandos específicos.
    * **Atomic Test ID (si aplica):** T1059.003 (ej. Atomic Test #1 - Command Execution).
    * **Propósito:** Entender cómo se identificaría la ejecución de comandos del sistema inusuales o potencialmente maliciosos en los logs.
    * **Results Esperados:** La ejecución de comandos `cmd.exe` generaría eventos en los logs del sistema y de seguridad (ej. Event ID 4688 con detalles de línea de comandos), así como posibles logs de Sysmon si está configurado.

### 2.3. Táctica: T1566 - Phishing

#### 2.3.1. Descripción de la Táctica
La táctica de Phishing es un vector de Acceso Inicial muy común, donde los adversarios intentan engañar a los usuarios para que revelen credenciales, instalen malware o hagan clic en enlaces maliciosos. Aunque la emulación de un phishing completo es compleja, se puede simular el resultado de una interacción de phishing, como la ejecución de un archivo malicioso entregado.

#### 2.3.2. Procedimiento de Simulación (Análisis Teórico)
Para comprender la simulación del impacto de un ataque de phishing exitoso, se analizaron las acciones que representarían la fase posterior a la interacción del usuario con un correo o enlace malicioso. El enfoque se puso en la ejecución de un archivo que simularía una carga útil inicial.

* **Ejecución de Archivo Malicioso (Simulado) (T1204.002 - User Execution: Malicious File):** Se investigó la emulación de la ejecución de un archivo (por ejemplo, un script PowerShell renombrado o un archivo batch) que simula la descarga o activación de una carga útil. Aunque no se descargaría malware real, se analizaría cómo se activarían acciones que un malware inicial podría realizar.
    * **Comando/Técnica Específica Esperada:** Un ejemplo teórico podría ser la ejecución de un archivo `.bat` simple que inicie un proceso benigno (`notepad.exe`) o un script PowerShell que simule un beacon HTTP básico.
    * **Atomic Test ID (si aplica):** T1204.002 (ej. Atomic Test #1 - User Execution - Shortcut File).
    * **Propósito:** Comprender cómo se detectaría la ejecución de archivos sospechosos iniciados por el usuario.
    * **Resultados Esperados:** La ejecución de un archivo malicioso simulado generaría eventos de creación de procesos (ej. Event ID 4688 si se inicia un nuevo proceso), y posibles eventos de red si el script intentara una conexión.

---
## 3. Metodología de Cacería de Amenazas (Threat Hunting)

La fase de cacería de amenazas se concibe como un proceso proactivo y metódico para identificar actividades maliciosas que podrían haber eludido las defensas automatizadas. Basándose en la comprensión teórica de las tácticas de emulación, esta sección detalla cómo se buscarían y analizarían los artefactos y logs generados. El objetivo es demostrar la capacidad de correlacionar la actividad del adversario con los datos de telemetría del sistema, incluso sin una ejecución directa de la simulación.

### 3.1. Herramientas Utilizadas (Análisis Teórico)
Desde una perspectiva de cacería de amenazas, las siguientes herramientas serían fundamentales para la recolección y el análisis de logs en un entorno Windows:

* **PowerShell:** Sería utilizado extensivamente para la recolección de información forense y para realizar consultas específicas sobre los datos de eventos y procesos. Comandos como `Get-WinEvent`, `Get-Process`, y `Get-Service` son esenciales para extraer datos relevantes del sistema en vivo o de logs exportados.
* **Visor de Eventos de Windows (Event Viewer):** Fundamental para revisar y filtrar los logs de seguridad, sistema y aplicación. Se analizarían los Event IDs específicos asociados con las tácticas de MITRE ATT&CK emuladas, buscando anomalías o indicadores de compromiso.
* **Herramientas SIEM/Análisis de Logs (Concepto):** En un entorno real, un SIEM (Security Information and Event Management) como Splunk, ELK Stack (Elasticsearch, Logstash, Kibana) o Microsoft Sentinel sería crucial para la ingesta centralizada, correlación y análisis de grandes volúmenes de datos de logs. Aquí se conceptualiza su rol en la cacería de amenazas para detectar patrones complejos y anomalías a escala.

### 3.2. Proceso de Búsqueda y Análisis de Evidencia (Análisis Teórico)
El proceso de búsqueda se basaría en la hipótesis de que las tácticas de emulación dejarían artefactos rastreables. La metodología incluiría:

1.  **Definición de Indicadores Clave (IOCs/IOAs):** Para cada táctica emulada, se identificarían los Indicadores de Compromiso (IOCs) o Indicadores de Ataque (IOAs) esperados, basándose en la documentación de MITRE ATT&CK y el análisis de comportamiento. Esto incluye Event IDs específicos, patrones de línea de comandos, cambios en el registro o en el sistema de archivos.
2.  **Consulta de Logs Relevantes:**
    * **Logs de Seguridad:** Especialmente importantes para la creación de cuentas (Event IDs 4720, 4722, 4732, 4738), inicio y fin de sesión (Event IDs 4624, 4634) y ejecución de procesos (Event ID 4688 si el auditing de línea de comandos está habilitado).
    * **Logs de Sistema:** Para eventos relacionados con servicios (ej., inicio/parada de WinRM o RDP).
    * **Logs de PowerShell:** Para la actividad detallada de scripts (si el Script Block Logging o Module Logging están activados).
3.  **Análisis de Anomalías y Correlación:** Una vez recolectados, los logs se analizarían buscando desviaciones del comportamiento normal del sistema. Se correlacionarían múltiples eventos para construir una línea de tiempo y comprender el "kill chain" simulado. Esto implicaría buscar secuencias de eventos que, individualmente, podrían ser benignos, pero que en conjunto indican actividad maliciosa.
4.  **Generación de Hipótesis y Refinamiento:** Basándose en los hallazgos iniciales, se formularían nuevas hipótesis de cacería, refinando las consultas y el enfoque para profundizar en la detección de la actividad emulada.

---
## 4. Hallazgos y Análisis de Evidencia (Enfoque Teórico)

Esta sección aborda los hallazgos anticipados y el análisis teórico de la evidencia que se esperaría encontrar tras la emulación de las tácticas de MITRE ATT&CK. El objetivo es detallar qué eventos y artefactos específicos buscaría un analista de seguridad y cómo se interpretarían para confirmar la actividad del adversario simulado.

### 4.1. Análisis por Táctica

#### 4.1.1. Táctica: TA0001 - Acceso Inicial (Initial Access)
* **Creación de Usuario Local (T1136.001):**
    * **Artefactos Esperados:**
        * **Event ID 4720:** Se registraría la creación de una nueva cuenta de usuario. Detalles importantes a verificar incluirían el `SubjectUserName` (quién creó la cuenta), `NewAccountName`, y el `SAMAccountName`.
        * **Event ID 4732:** Si la cuenta creada se agrega a un grupo local de seguridad (como "Administrators"), este evento lo registraría, mostrando la cuenta agregada (`Member Name`) y el grupo (`Target Group Name`).
        * **Event ID 4624:** Posible inicio de sesión de la nueva cuenta.
    * **Análisis Teórico:** La aparición de estos eventos para un usuario no autorizado o inesperado sería un fuerte indicador de compromiso inicial. Se correlacionarían estos eventos con la actividad de red o procesos inusuales para identificar el vector de acceso.

* **Habilitación de Servicios Remotos (ej. WinRM, RDP):**
    * **Artefactos Esperados:**
        * **Event ID 4719 / 4739 (Cambios de Política):** Podrían indicar modificaciones en las políticas de seguridad o configuraciones de firewall que habiliten los servicios.
        * **Event ID 7036 (Service Control Manager):** Registros de inicio o parada de servicios como "WinRM" o "Remote Desktop Services".
        * **Logs de Firewall de Windows:** Eventos indicando la apertura de puertos (ej. 5985 para WinRM, 3389 para RDP).
    * **Análisis Teórico:** La activación inesperada de estos servicios, especialmente si no está justificada por cambios legítimos en la configuración, indicaría la preparación del adversario para la persistencia o el movimiento lateral. La línea de tiempo de los eventos sería crucial para determinar cuándo y por qué se habilitaron.

#### 4.1.2. Táctica: T1059 - Intérprete de Comandos y Scripts (Command and Scripting Interpreter)
* **Ejecución de Comandos con PowerShell (T1059.001):**
    * **Artefactos Esperados:**
        * **Event ID 4688 (Creación de Procesos):** Si el "Process Creation Auditing" está habilitado, mostraría `powershell.exe` como un nuevo proceso, incluyendo la `CommandLine` completa con los argumentos y scripts ejecutados (especialmente útil si se habilita el auditing de línea de comandos).
        * **Event ID 4104 (PowerShell Script Block Logging):** El registro de bloques de script PowerShell capturaría scripts completos o partes de ellos, incluso si están ofuscados. Esto es invaluable para entender la intención del adversario.
    * **Análisis Teórico:** La presencia de `powershell.exe` con comandos inusuales, codificados o descargando contenido externo sería un indicador crítico. Se buscarían patrones de ejecución atípicos (ej. PowerShell sin una ventana de consola, o ejecutándose desde directorios temporales).

* **Ejecución de Comandos del Sistema (T1059.003 - Cmd):**
    * **Artefactos Esperados:**
        * **Event ID 4688 (Creación de Procesos):** Registraría `cmd.exe` y sus argumentos de línea de comandos (`CommandLine`). Se buscarían comandos como `whoami`, `ipconfig`, `netstat`, `dir` en directorios inusuales, o comandos para crear/modificar archivos.
    * **Análisis Teórico:** La ejecución de comandos del sistema por parte de procesos inesperados o en momentos atípicos (ej. fuera de horario laboral) requeriría investigación. La correlación con la actividad de red o de otros procesos ayudaría a construir el contexto del ataque.

#### 4.1.3. Táctica: T1566 - Phishing
* **Ejecución de Archivo Malicioso (Simulado) (T1204.002):**
    * **Artefactos Esperados:**
        * **Event ID 4688 (Creación de Procesos):** La ejecución del archivo simulado (ej. `notepad.exe` o un script `.bat` o `.ps1`) generaría un evento de creación de proceso, mostrando el `New Process Name` y la `CommandLine` completa.
        * **Event ID 1 (Sysmon - Process Create):** Si Sysmon estuviera instalado y configurado, proporcionaría información más rica sobre la creación de procesos, incluyendo el proceso padre, la línea de comandos, el hash del archivo y la información del usuario.
        * **Eventos de Red (si aplica):** Si el script simulado intentara una conexión de red (ej. un beacon HTTP a un C2 simulado), se registrarían eventos de conexión de red (ej. Event ID 5156 para Windows Firewall, o logs de Sysmon Event ID 3).
    * **Análisis Teórico:** La aparición de un proceso inesperado iniciado por un usuario (especialmente si no es un proceso conocido del sistema o de una aplicación legítima) sería un hallazgo clave que indicaría la ejecución exitosa del vector de phishing. La correlación con la actividad de red o la creación de archivos sospechosos sería crucial.

---
## 5. Conclusiones y Recomendaciones (Enfoque Teórico)

Este ejercicio teórico de emulación de amenazas y cacería (threat hunting) ha proporcionado una comprensión invaluable sobre las dinámicas ofensivas y defensivas en el panorama de la ciberseguridad. A pesar de no haber sido ejecutado en un entorno práctico, el análisis detallado de las tácticas de MITRE ATT&CK® y los artefactos de log esperados ha solidificado el conocimiento sobre cómo los adversarios operan y, más importante aún, cómo sus acciones pueden ser detectadas y analizadas.

### 5.1. Conclusiones Clave

* **Comprensión Profunda de Tácticas Adversarias:** El estudio de tácticas como Acceso Inicial, Intérprete de Comandos y Scripts, y Phishing, en el contexto de Atomic Red Team, ha permitido una visión clara de los pasos que un atacante podría seguir y las herramientas que utilizaría. Esto es fundamental para cualquier analista de SOC, ya que ayuda a pensar como el adversario.
* **Importancia de la Telemetría y Logging:** Se ha reafirmado la criticidad de una telemetría robusta y una configuración de logging exhaustiva. Sin eventos detallados (como el Process Creation Auditing con línea de comandos, o PowerShell Script Block Logging), la cacería de amenazas se vuelve extremadamente difícil. Los Event IDs específicos identificados son esenciales para una detección efectiva.
* **Rol de la Cacería de Amenazas Proactiva:** Este ejercicio resalta que depender únicamente de las soluciones de seguridad automatizadas no es suficiente. La cacería de amenazas proactiva, guiada por el conocimiento de tácticas adversarias y el análisis de logs, es indispensable para descubrir amenazas sofisticadas que podrían evadir las detecciones iniciales.
* **Utilidad de MITRE ATT&CK®:** El marco ATT&CK se demuestra como una herramienta invaluable para estructurar la emulación de amenazas, entender el comportamiento del adversario y guiar la cacería de amenazas. Proporciona un lenguaje común y una base de conocimiento para categorizar y analizar las amenazas.

### 5.2. Recomendaciones Teóricas para la Defensa y Detección

Basándose en el análisis de las tácticas emuladas y los artefactos esperados, se formulan las siguientes recomendaciones para fortalecer las capacidades de detección y respuesta en un entorno Windows:

1.  **Habilitar Auditing Avanzado:** Es fundamental configurar y monitorear el auditing de seguridad avanzado en Windows, especialmente:
    * **Auditing de Creación de Procesos (Event ID 4688) con línea de comandos:** Esto captura los detalles completos de los comandos ejecutados, que son críticos para identificar scripts maliciosos o usos anómalos de cmd.exe o PowerShell.
    * **PowerShell Script Block Logging (Event ID 4104):** Para registrar el contenido de los scripts PowerShell ejecutados, incluso si están ofuscados.
    * **Auditing de Cambios en Grupos de Seguridad:** Para detectar la adición de usuarios a grupos privilegiados.
2.  **Implementar Sysmon:** Desplegar y configurar Sysmon (System Monitor) con una configuración robusta para obtener una telemetría de procesos, red y archivos mucho más rica y detallada que la que ofrecen los logs nativos de Windows.
3.  **Monitoreo y Alerta sobre Eventos Críticos:** Establecer alertas basadas en los Event IDs específicos y patrones de comportamiento relacionados con las tácticas analizadas (ej., creación de usuarios privilegiados fuera de horario, ejecución de PowerShell codificado, habilitación inesperada de servicios remotos).
4.  **Integración SIEM:** Para entornos a gran escala, la ingesta de todos los logs relevantes en una plataforma SIEM es crucial. Esto permite la correlación avanzada de eventos, la visualización de datos y la automatización de alertas, mejorando significativamente la eficiencia de la cacería de amenazas.
5.  **Entrenamiento Continuo:** Capacitar al personal de seguridad en el marco MITRE ATT&CK®, en técnicas de emulación de amenazas, y en el uso de herramientas de cacería (como PowerShell y Sysmon) es esencial para desarrollar habilidades proactivas de detección.
6.  **Realizar Ejercicios Periódicos de Red Team/Purple Team:** La práctica de ejercicios de emulación (incluso simulaciones teóricas detalladas como esta) combinados con la cacería de amenazas ayuda a validar la postura de seguridad, identificar brechas en la detección y mejorar los procesos de respuesta a incidentes.

---
## 6. Anexos (Referencias a la Evidencia Conceptual)

Esta sección de Anexos serviría como un repositorio centralizado para toda la evidencia técnica generada durante un ejercicio práctico de emulación de amenazas y cacería (threat hunting). Aunque este informe se basa en un análisis teórico, se conceptualiza la inclusión de los siguientes tipos de artefactos para una documentación completa y reproducible.

* **Registros de Eventos (Event Logs):**
    * **Logs de Seguridad:** Exportaciones filtradas de eventos relacionados con la creación de procesos (Event ID 4688), autenticación (Event ID 4624, 4634), creación y modificación de cuentas (Event ID 4720, 4732), y otros eventos de seguridad relevantes.
    * **Logs de PowerShell:** Si el Script Block Logging o el Module Logging estuvieran activados, se incluirían los logs detallados de la ejecución de scripts maliciosos o sospechosos (Event ID 4104).
    * **Logs de Sysmon:** Registros detallados de la actividad de procesos, conexiones de red, creaciones de archivos, etc., que proporcionarían una visibilidad granular de las acciones emuladas.
    * **Ubicación Conceptual:** [`informe/anexos/logs/`](./anexos/logs/)

* **Capturas de Pantalla (Screenshots):**
    * **Evidencia de Ejecución de Tácticas:** Capturas de pantalla de la línea de comandos o PowerShell durante la ejecución de los Atomic Tests, mostrando la sintaxis y la salida (si aplica).
    * **Hallazgos de Cacería:** Imágenes del Visor de Eventos de Windows resaltando Event IDs clave, resultados de consultas PowerShell, o visualizaciones en una herramienta SIEM (si fuera el caso práctico) que demuestren la detección de las actividades emuladas.
    * **Ubicación Conceptual:** [`informe/anexos/screenshots/`](./anexos/screenshots/)

* **Scripts Utilizados (Referencia):**
    * Aunque el informe detallaría las técnicas, se haría referencia a los scripts específicos de Atomic Red Team o scripts personalizados de PowerShell utilizados para la emulación y la cacería.
    * **Ubicación de Scripts:** [`scripts/atomic_red_team/`](../../scripts/atomic_red_team/) y [`scripts/threat_hunting/`](../../scripts/threat_hunting/)
