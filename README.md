# Network Security Log Analyzer

## Overview
A Python-based cybersecurity project that analyzes simulated authentication logs to identify failed login attempts and flag potentially suspicious IP addresses.

## Features
- Counts successful and failed login attempts.
- Groups failed login attempts by IP address.
- Detects suspicious IP addresses using a configurable threshold.
- Generates a text report automatically.

## Technologies
- Python 3
- PowerShell
- Git and GitHub

## How to Run
1. Open PowerShell in the project folder.
2. Run:

   python log_analyzer.py

3. View the generated report at `reports/analysis_report.txt`.

## Detection Logic
The default threshold is 3 failed login attempts per IP address. Change the `threshold` variable in `log_analyzer.py` to adjust it.

## Sample Data
The project uses simulated authentication logs for educational purposes. The IP addresses in the sample logs are reserved documentation addresses, not real attack sources.

## Disclaimer
This project is for educational and defensive cybersecurity practice only.
