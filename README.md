# Cybersecurity Operations (SOC) Portfolio - Ruben Rodriguez Roman

Welcome to my Cybersecurity Operations (SOC) Portfolio! This repository showcases practical projects, vulnerability reports, and **adversary emulation exercises**, demonstrating my growing skills and hands-on experience in the cybersecurity field.

I'm actively learning and applying concepts in network security, vulnerability management, and incident response, striving to contribute effectively to a Security Operations Center environment.

---

## Projects & Reports

Here's an overview of the key projects and reports housed within this portfolio:

### Week 1: Foundational Labs
This section contains my initial hands-on exercises, covering foundational cybersecurity and networking concepts. It includes:
- 🔍 **Apache Log Analysis:** Practical exercises focused on interpreting and analyzing Apache web server logs to identify security events.
- 🐧 **Practical Linux Exercises (Bandit):** Notes and solutions from the Bandit Wargame, enhancing my command-line proficiency and understanding of Linux fundamentals.
- **Location:** [`Semana1/`](./Semana1/)

### Nessus Vulnerability Assessment Reports
This section features practical experience with **Tenable Nessus Essentials**, a leading vulnerability scanner. It includes detailed reports on identifying, analyzing, and proposing remediations for discovered vulnerabilities.

#### Node.js Outdated Version Vulnerability (Critical)
- **Description:** A comprehensive report on a critical vulnerability identified in an outdated Node.js version running on a Kali Linux virtual machine. This report details the vulnerability's nature, its potential impact, and the recommended solutions to mitigate the risk.
- **Report (Spanish):** [`reporte_vulnerabilidad_nodejs.md`](./Nessus/reporte_vulnerabilidad_nodejs.md)
- **Report (English):** [`vulnerability_report_nodejs_en.md`](./Nessus/vulnerability_report_nodejs_en.md)
    *(Located in the `Nessus/` folder)*

---

### Threat Emulation Report - Red Team Atomic (Compensatory Project)
This section documents a comprehensive threat emulation exercise. Conducted as a compensatory project for an advanced cybersecurity course, its primary goal was to simulate specific adversary tactics using **Atomic Red Team** frameworks and then perform **threat hunting** to detect evidence of these activities within a Windows environment.

**Project Focus:**
This project delves into the practical application of **MITRE ATT&CK®** tactics, specifically:
* **TA0001 - Initial Access**: Exploring methods an adversary might use to gain initial entry into a system.
* **T1059 - Intérprete de Comandos y Scripts (Command and Scripting Interpreter)**: Simulating the execution of commands and scripts by an attacker for various malicious purposes.
* **T1566 - Phishing**: Emulating a phishing attempt as a common initial access vector to compromise user credentials or trigger malware execution.

The project also features a **threat hunting** component, utilizing **PowerShell** for active querying and **Windows Event Viewer (Event Logs)** for forensic analysis to search for indicators of compromise (IOCs).

**Project Location:** [`threat-emulation-report/`](./threat-emulation-report/)

*(For the Spanish version of this report's overview, please refer to the `README_ES.md` within the `threat-emulation-report/` directory.)*

---

## Skills Demonstrated

* **Linux:** Advanced navigation, log analysis, command-line operations.
* **Threat Emulation:** Practical experience with **Atomic Red Team** for simulating adversary tactics.
* **Threat Hunting:** Proficiency in using **PowerShell** and **Windows Event Viewer** for forensic analysis and detection of malicious activity.
* **MITRE ATT&CK® Framework:** Applied understanding of various tactics (Initial Access, Command and Scripting Interpreter, Phishing) for both offensive simulation and defensive detection.
* **Incident Response Fundamentals:** Experience in identifying, analyzing, and documenting security incidents based on simulated attacks.
