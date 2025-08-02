# NPONTU App Performance Analysis – Assignment

This repository contains my technical assignment submission for the **App/Ops Officer Intern** role at **NPONTU Technologies**.

---

## Assignment Summary

The task involved analyzing a set of application logs to identify the root cause of a performance issue and creating a **runbook** to troubleshoot similar problems in the future.

### Issue Identified:
The application was experiencing **repeated crashes** during report generation due to a **memory leak**. Logs indicated increasing memory usage leading to process termination.

---

## Files Included

| File Name                    | Description |
|-----------------------------|-------------|
| `npontu_assignment_memory_leak.md` | Main report with logs, root cause analysis, and troubleshooting steps |
| `sample_logs.txt`           | Sample application logs used for the analysis |
| `memory_leak_demo.py`       | Python simulation of a memory leak (for demonstration) |
| `README.md`                 | This file – summarizes the project |

---

## Demo Script: `memory_leak_demo.py`

This script simulates a memory leak by appending large strings to a global list in an infinite loop. It demonstrates how unchecked memory usage can impact performance over time.

```python
leaky_list = []

def generate_report():
    for _ in range(100000):
        leaky_list.append("LargeData" * 1000)
