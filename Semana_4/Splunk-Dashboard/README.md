# Proyecto Splunk: Dashboard de Monitoreo de Autenticación (Semana 4 - Día 22)

## Introducción
Este proyecto demuestra la habilidad de utilizar un SIEM (Splunk Enterprise) para transformar logs brutos en inteligencia de seguridad accionable a través de un Dashboard. El objetivo fue monitorear la actividad de fuerza bruta en los logs de autenticación de un sistema Linux.

## Metodología
1.  **Herramienta:** Splunk Enterprise (Free License).
2.  **Ingesta de Datos:** Se importó el archivo `auth_log_analysis.log`.
3.  **Lenguaje de Búsqueda (SPL):** Se utilizaron comandos SPL avanzados (`timechart`, `stats count`, `sort`) para la agregación y visualización de datos.

## Consultas SPL Utilizadas

### 1. Fallos de Autenticación a lo Largo del Tiempo (Timechart)
Esta consulta muestra la cronología de los eventos para identificar picos de actividad:
```spl
index=main source="auth_log_analysis.log" "authentication failure" | timechart count
