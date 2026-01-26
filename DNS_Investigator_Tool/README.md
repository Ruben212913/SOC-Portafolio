# 🔍 DNS & OSINT Investigator Tool

## 🇪🇸 Descripción (Español)
Esta herramienta es un script de Python diseñado para realizar investigaciones de **OSINT (Open Source Intelligence)** y análisis de red. Permite a los analistas SOC identificar rápidamente la procedencia de una dirección IP o un dominio mediante consultas de DNS inverso y resolución de nombres.

### 🛠️ Características:
* **Resolución Inversa (Reverse Lookup):** Obtiene el nombre de host a partir de una dirección IP.
* **Resolución Directa:** Identifica las IPs asociadas a un dominio.
* **Análisis por Lotes:** Capacidad para procesar múltiples objetivos en una sola ejecución.
* **Uso en SOC:** Ideal para investigar IPs sospechosas detectadas en alertas de SIEM o firewalls.

---

## 🇺🇸 Description (English)
This tool is a Python script designed for **OSINT (Open Source Intelligence)** and network analysis. It allows SOC Analysts to quickly identify the origin of an IP address or domain through reverse DNS queries and name resolution.

### 🛠️ Features:
* **Reverse Lookup:** Retrieves the hostname from an IP address.
* **Forward Resolution:** Identifies IP addresses associated with a domain.
* **Batch Analysis:** Capability to process multiple targets in a single run.
* **SOC Use Case:** Perfect for investigating suspicious IPs detected in SIEM or firewall alerts.

---

## 🚀 Cómo usar / How to use

1. **Requisitos:** Tener Python 3 instalado.
2. **Ejecución:**
   ```bash
   python3 src/dns_investigator.py
