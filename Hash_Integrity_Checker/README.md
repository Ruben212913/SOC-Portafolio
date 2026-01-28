# 🔐 Hash Integrity Checker

## 🇪🇸 Descripción
Esta herramienta permite a un Analista SOC verificar la integridad de archivos sospechosos o críticos. Al generar un hash **SHA-256**, podemos confirmar si un archivo ha sido alterado por un atacante o si coincide con firmas de malware conocidas.

### 🛠️ Características:
* **Algoritmo SHA-256:** El estándar de la industria para integridad.
* **Lectura Binaria:** Compatible con cualquier tipo de archivo (.exe, .pdf, .jpg, etc.).
* **Fase SOC:** Se utiliza en la fase de **Análisis Forense**.

---

## 🇺🇸 Description
This tool allows a SOC Analyst to verify the integrity of suspicious or critical files. By generating a **SHA-256** hash, we can confirm if a file has been altered by an attacker or if it matches known malware signatures.

### 🛠️ Features:
* **SHA-256 Algorithm:** Industry standard for integrity.
* **Binary Reading:** Compatible with any file type.
* **SOC Phase:** Used in the **Forensics/Analysis** phase.

---

## 🚀 Uso / Usage
1. Ejecuta el script: `python3 src/hash_checker.py`
2. Introduce la ruta del archivo que quieres verificar.
3. Compara el hash resultante.

**Evidencia:** ![Hash Evidence](docs/evidence.png)
