# 🛡️ Protocolo de Respuesta a Incidentes (SOC Nivel 1)

Este documento define el orden de operaciones y el uso de herramientas desarrolladas en este portafolio ante una alerta de seguridad.

## ⏱️ Fase 1: Detección y Visibilidad (Monitoreo)
**Herramienta:** `Network_Traffic_Analyzer`
**Cuándo usarla:** Tan pronto como el SIEM (Splunk) lanza una alerta de tráfico inusual.
* **Objetivo:** Capturar paquetes crudos (.pcap) para ver qué está pasando realmente en el cable.
* **Pregunta clave:** ¿Qué protocolo están usando y cuántos datos se están enviando?

## 🔎 Fase 2: Análisis y Contextualización (Investigación)
**Herramienta:** `DNS_Investigator_Tool`
**Cuándo usarla:** Inmediatamente después de obtener la IP sospechosa del paso anterior.
* **Objetivo:** Identificar al propietario de la IP y la reputación del dominio.
* **Pregunta clave:** ¿Es esta IP de un servidor conocido o es un dominio malicioso recién creado?

## 🔐 Fase 3: Verificación de Integridad (Forense)
**Herramienta:** `Hash_Integrity_Checker`
**Cuándo usarla:** Si se detecta que el atacante subió o modificó archivos en el sistema.
* **Objetivo:** Comparar firmas digitales de archivos para detectar malware o alteraciones.
* **Pregunta clave:** ¿Ha sido este archivo modificado por el atacante?

---
**Nota:** Este flujo sigue los estándares de **NIST SP 800-61** para la gestión de incidentes de ciberseguridad.
