# Threat Emulation Report - Red Team Atomic (Compensatory Project)

This repository contains documentation related to a threat emulation exercise conducted as a compensatory project for an advanced cybersecurity course. The primary goal of this project was to simulate specific adversary tactics using **Atomic Red Team** frameworks and then perform **threat hunting** to detect evidence of these activities within a Windows environment.

## Project Overview

This project focuses on the practical application of **MITRE ATT&CK®** tactics, specifically:

* **TA0001 - Initial Access**: Exploring methods an adversary might use to gain initial entry into a system.
* **T1059 - Command and Scripting Interpreter**: Simulating the execution of commands and scripts by an attacker for various malicious purposes.
* **T1566 - Phishing**: Emulating a phishing attempt as a common initial access vector to compromise user credentials or trigger malware execution.

The second core component of this project involves **threat hunting**. Using **PowerShell** for active querying and **Windows Event Viewer (Event Logs)** for forensic analysis, this section details the process of searching for indicators of compromise (IOCs) left behind by the simulated attacks.

## Tools and Technologies

The following key tools and technologies were leveraged throughout this project:

* **Atomic Red Team**: Utilized for executing predefined adversary emulation tests that map to MITRE ATT&CK tactics.
* **PowerShell**: Employed for both the execution of malicious-like commands during the emulation phase and for performing comprehensive threat hunting queries on the system.
* **Windows Event Viewer (Event Logs)**: Crucial for analyzing system activity, identifying security events, and correlating logs to detect evidence of the simulated attacks.

## Repository Structure and Navigation

This repository is organized to provide a clear overview of the threat emulation project. Here's a breakdown of its key directories and their contents:

* **`README.md` / `README_ES.md`**: These files serve as the main entry points, providing an overview of the project in English and Spanish, respectively.
* **`docs/`**: Contains supplementary documentation, such as attack plans or scenario definitions, relevant to the project's setup and execution.
* **`informe/`**: Houses the main project report (`informe_final.md`), which details the simulated tactics, threat hunting methodology, findings, and conclusions. This directory also includes the `anexos/` subfolder, where all raw logs (PowerShell outputs, Event Viewer exports) and screenshots are stored as evidence.
* **`scripts/`**: Contains all PowerShell scripts used during the project. This is further categorized into:
    * **`atomic_red_team/`**: Scripts specifically used for emulating MITRE ATT&CK tactics (e.g., `T1059_cmd_exec.ps1`).
    * **`threat_hunting/`**: Scripts developed for searching and analyzing system logs and indicators during the threat hunting phase (e.g., `search_event_logs.ps1`).

To access the detailed report, navigate to the `informe/` directory and open `informe_final.md`. All supporting evidence can be found within `informe/anexos/`.

---
For the Spanish version of this README, please refer to [README_ES.md](README_ES.md).
---
