# Threat Emulation and Hunting Report

## 1. Introduction

This report documents a threat emulation and hunting exercise conducted as a compensatory project for an advanced cybersecurity course. The primary objective was to apply theoretical knowledge in a practical scenario, simulating real-world adversary tactics and developing skills for their detection.

The exercise focused on emulating specific tactics from the **MITRE ATT&CK® framework**, including **Initial Access (TA0001)**, the use of the **Command and Scripting Interpreter (T1059)**, and the **Phishing (T1566)** tactic as an entry vector. Following the simulation of these offensive activities, an active threat hunting phase was conceptualized, utilizing tools like **PowerShell** and the **Windows Event Viewer**, to identify and analyze the expected evidence of the emulated actions.

The purpose of this report is to detail the theoretical methodology used, the simulation procedures, the applied hunting techniques, and the anticipated findings, thereby demonstrating the ability to understand, simulate, and detect malicious activities in a network environment.

---

## 2. Threat Emulation Methodology

The threat emulation phase of this project was designed to conceptually understand real adversary behavior, utilizing techniques and tools aligned with the MITRE ATT&CK® framework. The goal was to document the theoretical knowledge of how these specific actions would be replicated to generate detectable artifacts in a Windows environment. For this, the main use of **Atomic Red Team**, a testing library that allows the execution of small and controlled simulations of attack tactics, was analyzed.

Each tactic was investigated from a theoretical perspective, understanding how it would be executed in a controlled laboratory environment (a vulnerable Windows virtual machine), the commands involved, and the events expected to be generated for subsequent detection.

### 2.1. Tactic: TA0001 - Initial Access

#### 2.1.1. Tactic Description
The Initial Access tactic represents the vectors adversaries use to gain their initial foothold in a network or system. This can include the use of stolen credentials, exploitation of external vulnerabilities, or malware delivery via phishing. For this exercise, we focused on analyzing how common initial compromise scenarios that would leave a digital footprint would be simulated.

#### 2.1.2. Simulation Procedure (Theoretical Analysis)
From a theoretical standpoint, to simulate Initial Access, the following controlled actions would be understood, using Atomic Red Team (or custom PowerShell scripts) to replicate typical attacker behaviors after gaining initial access:

* **Local User Creation (T1136.001 - Create Account: Local Account):** The simulation of creating a privileged local user account was investigated. This represents a common step for adversaries to establish persistence once inside.
    * **Expected Specific Command/Technique:** `net user [username] [password] /add` and `net localgroup administrators [username] /add`.
    * **Atomic Test ID (if applicable):** T1136.001 (e.g., Atomic Test #1 - Create Local User).
    * **Purpose:** To understand the detection of unauthorized account creation in security logs.
    * **Expected Results:** The creation of a new user and its addition to a privileged group would generate specific events in the Windows Event Viewer (e.g., Event ID 4720 for user creation, Event ID 4732 for addition to a local security group).

* **Enabling Remote Services (e.g., WinRM, RDP):** The emulation of modifying service configurations to allow remote access was analyzed, a common post-exploitation action to facilitate lateral movement or persistence.
    * **Expected Specific Command/Technique:** PowerShell commands to enable WinRM (`winrm quickconfig`) or RDP.
    * **Atomic Test ID (if applicable):** Atomic Red Team may offer tests like T1021.001 (RDP) or T1021.006 (WinRM).
    * **Purpose:** To understand how the suspicious activation of remote access services would be identified in system logs.
    * **Expected Results:** Modifying service configurations would generate events in system logs, indicating changes in firewall settings or service starts.

### 2.2. Tactic: T1059 - Command and Scripting Interpreter

#### 2.2.1. Tactic Description
The Command and Scripting Interpreter tactic involves using command-line interfaces (CLI) or scripting languages (such as PowerShell, Bash, Python) to execute commands that can manipulate systems, download and execute payloads, or interact with the operating system in various malicious ways. This tactic is fundamental for most adversaries, as it allows them to operate directly on the compromised system.

#### 2.2.2. Simulation Procedure (Theoretical Analysis)
To understand the emulation of using command and scripting interpreters, it was investigated how Atomic Tests would be executed to simulate how an attacker might use PowerShell or the command line to perform post-exploitation actions:

* **Executing Commands with PowerShell (T1059.001 - PowerShell):** The simulation of executing obfuscated or encoded PowerShell commands was analyzed. This represents the common use of PowerShell by adversaries for reconnaissance, persistence, or lateral movement.
    * **Expected Specific Command/Technique:** Examples include `powershell.exe -EncodedCommand ...` or the use of `Invoke-AtomicTest T1059.001` for specific scenarios.
    * **Atomic Test ID (if applicable):** T1059.001 (e.g., Atomic Test #2 - PowerShell Remote Command Execution).
    * **Purpose:** To understand the detection of PowerShell execution and suspicious commands through process and command-line argument monitoring.
    * **Expected Results:** PowerShell execution would generate events in security logs (e.g., Event ID 4688 with command-line details if auditing is enabled, or PowerShell Script Block Logging).

* **Executing System Commands (T1059.003 - Cmd):** The emulation of executing `cmd.exe` commands that adversaries use for tasks like network enumeration, file manipulation, or system interaction was investigated.
    * **Expected Specific Command/Technique:** Examples include `cmd.exe /c
