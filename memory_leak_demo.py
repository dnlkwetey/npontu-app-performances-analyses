# NPONTU App Performance Analysis – Assignment

This project is my submission for the **App/Ops Officer Intern** position at **NPONTU Technologies**.

## Assignment Overview

I analyzed a performance issue using sample application logs. The problem was caused by a memory leak during the `/generate-report` operation, leading to high memory usage and frequent server crashes.

## Files Included

- `npontu_assignment_memory_leak.md` — Full report including:
  - Sample logs
  - Root cause analysis
  - A detailed runbook for troubleshooting
---
[2025-07-25 09:00:01] INFO: API server started on port 8000
[2025-07-25 09:15:22] INFO: Received request to /generate-report
[2025-07-25 09:15:23] INFO: Report generation started for userID: 104
[2025-07-25 09:15:33] WARN: Memory usage crossed 85%
[2025-07-25 09:15:36] ERROR: Out of memory - process killed
[2025-07-25 09:15:38] INFO: Application restarting... 
[2025-07-25 09:25:10] INFO: Received request to /generate-report
[2025-07-25 09:25:20] WARN: Memory usage crossed 90%
[2025-07-25 09:25:25] ERROR: Out of memory - process killed

---

## Root Cause Analysis

The memory usage increased significantly every time the `/generate-report` endpoint was triggered. Eventually, the process exceeded the system’s memory limit and was terminated.

### Cause:  
A **memory leak** was detected, possibly due to large objects or data structures not being released.

---

## Runbook: Troubleshooting Memory Leaks in Web Apps

### 1. Identify Symptoms
- App restarts frequently  
- Logs show memory warnings/errors  
- Specific endpoints crash the app  

### 2. Analyze Logs and Code
- Focus on log timestamps around crashes  
- Review code for:
  - Unreleased objects (open files, DB connections)
  - Growing data structures

# memory_leak_demo.py

import time

# Simulated memory leak using a list that never gets cleared
leaky_list = []

def generate_report_simulation():
    print("Starting report generation...")
    for i in range(100000):
        leaky_list.append("Some large data " * 1000)  # Simulate large memory use
        if i % 10000 == 0:
            print(f"Generated part {i}, memory growing...")

    print("Report generation complete.")

if __name__ == "__main__":
    try:
        while True:
            generate_report_simulation()
            time.sleep(2)  # Wait before generating again
    except KeyboardInterrupt:
        print("Process stopped by user."
