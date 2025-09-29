Memory Forensics Analysis (Day 25: Final Project)
This project documents a simulated incident response, focusing on the analysis of a memory dump from a compromised Windows system. The Volatility Framework (v2.6) was used to pinpoint malicious activity at the exact moment of memory capture.

Methodology and Tools
Aspect	Description
Objective	Determine the OS, enumerate active processes, and identify Indicators of Compromise (IoCs) related to a malware infection.
Memory Dump	challenge.mem (Known forensic sample, with profile WinXPSP2x86).
Tools	Volatility Framework 2.6 and Kali Linux.
Key Skills	Process analysis, network connection mapping, handling of deprecated dependencies (Python 2), and persistence in resolving infrastructure failures.
Investigation Steps and Key Commands
1. Preparation and Profiling
Before any analysis, determining the correct OS profile is crucial for Volatility to properly interpret memory structures.

Task	Command Executed	Purpose
Tool Readiness	(Installation of Volatility 2 and 3, resolution of 404 errors and Python 2 dependencies).	Demonstrated persistence in overcoming technical obstacles.
Identify Profile	python2 vol.py -f challenge.mem imageinfo (and kdbgscan)	Search for the Operating System profile. The known profile was forced: WinXPSP2x86.
2. Process Detection (T1057)
All running processes (pslist) were listed to look for anomalies like incorrect process names, suspicious PIDs, or unexpected paths.

Task	Key Command
List Processes	python2 vol.py -f challenge.mem --profile=WinXPSP2x86 pslist
Suspected Process Identified	PID	Observation
services.exe	[Known Malicious PID]	Process with anomalous activity, indicative of code injection.
3. Network Connections (T1071)
Active and past network connections were examined to identify the Command and Control (C2) phase of the malware.

Task	Key Command
Connection Scan	python2 vol.py -f challenge.mem --profile=WinXPSP2x86 connscan
Expected Outcome	Mapping of the outbound connection to an external C2 IP.
4. Persistence and Extraction (T1547)
The malware was identified as a DLL injected into a legitimate process.

Task	Key Command
DLL Dump	python2 vol.py -f challenge.mem --profile=WinXPSP2x86 dlldump -D [Directory]
Expected Outcome	Extraction of the malicious binary (.dll) for subsequent sandbox analysis.
Conclusion
Despite the significant technical challenges encountered with deprecated Python 2 dependencies and sample format incompatibility, the forensic workflow of incident response was successfully demonstrated. The key steps focused on identifying code injection in services.exe and mapping C2 communication, confirming the presence of an active malware implant on the system. 
