# 💻 DAY 25-26: MEMORY FORENSICS ANALYSIS (FINAL PROJECT)

This project documents a simulated incident response, focusing on the **analysis of a memory dump** from a compromised Windows system. The **Volatility Framework** was used to confirm and characterize the malicious activity.

## Methodology and Tools

| Aspect | Detail |
| :--- | :--- |
| **Objective** | Determine the OS profile, enumerate active processes, and identify Indicators of Compromise (IoCs) from a malware infection. |
| **Memory Dump** | `challenge.mem` (Known forensic sample, profile **WinXPSP2x86**). |
| **Tools** | **Volatility Framework 2.6** and **Kali Linux**. |
| **Key Skills** | Process analysis (T1057), network connection mapping (T1071), handling deprecated dependencies (Python 2), and persistence in resolving infrastructure failures. |

## Key Findings

The analysis confirmed an active infection with a Trojan that utilized:

1.  **Code Injection (T1055):** Hiding within the legitimate process **`services.exe`**.
2.  **Command and Control (C2):** Established an outbound connection to an external IP address.
3.  **Persistence (T1547):** Used files or registry keys to ensure reboot survival.

**The detailed technical report of these findings is available in the file `Reporte_Final_Malware.md`.**
