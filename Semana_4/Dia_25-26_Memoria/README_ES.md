# 💻 DÍA 25-26: ANÁLISIS FORENSE DE MEMORIA (PROYECTO FINAL)

Este proyecto documenta la respuesta a un incidente simulado, centrándose en el **análisis de un volcado de memoria (Memory Dump)** de un sistema Windows comprometido.

## Metodología y Herramientas

| Aspecto | Detalle |
| :--- | :--- |
| **Objetivo** | Determinar el sistema operativo, enumerar procesos activos e identificar indicadores de compromiso (IoCs) de una infección de malware. |
| **Volcado de Memoria** | `challenge.mem` (Muestra forense conocida, perfil **WinXPSP2x86**). |
| **Herramientas** | **Volatility Framework 2.6** y **Kali Linux**. |
| **Habilidades Clave** | Análisis de procesos (T1057), identificación de conexiones de red (T1071), manejo de dependencias obsoletas (Python 2), y resolución de fallos de infraestructura. |

## Hallazgos Clave

El análisis confirmó una infección activa con un troyano que utilizó:

1.  **Inyección de Código (T1055):** Ocultamiento en el proceso legítimo **`services.exe`**.
2.  **Comando y Control (C2):** Establecimiento de una conexión saliente a una IP externa.
3.  **Persistencia (T1547):** Uso de archivos o claves de registro para asegurar el reinicio.

**El reporte técnico detallado de estos hallazgos se encuentra en el archivo `Reporte_Final_Malware.md`.**
