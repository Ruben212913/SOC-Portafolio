# Splunk Project: Authentication Monitoring Dashboard (Week 4 - Day 22)

## Introduction
This project demonstrates the ability to utilize a Security Information and Event Management (SIEM) tool, specifically **Splunk Enterprise**, to transform raw logs into actionable security intelligence via a Dashboard. The objective was to monitor for potential brute-force activity in Linux authentication logs.

## Methodology
1.  **Tool:** Splunk Enterprise (Free License).
2.  **Data Ingestion:** The `auth_log_analysis.log` file was successfully imported and indexed into Splunk.
3.  **Search Language (SPL):** Advanced Search Processing Language commands were used for data aggregation and visualization, including `timechart`, `stats count`, and `sort`.

## Search Processing Language (SPL) Queries Used

### 1. Authentication Failures Over Time (Timechart)
This query provides a timeline of events, allowing a SOC analyst to identify spikes and trends in activity:
```spl
index=main source="auth_log_analysis.log" "authentication failure" | timechart count
