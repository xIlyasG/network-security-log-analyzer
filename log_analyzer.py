threshold = 3

success_count = 0
failed_count = 0
failed_by_ip = {}

with open("sample_logs.txt", "r") as file:
    for line in file:
        if "LOGIN_SUCCESS" in line:
            success_count += 1

        if "LOGIN_FAILED" in line:
            failed_count += 1
            parts = line.split()
            ip = parts[-1].split("=")[1]
            failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1

report_lines = [
    "NETWORK SECURITY LOG ANALYSIS REPORT",
    "====================================",
    f"Detection threshold: {threshold} failed attempts",
    f"Successful logins: {success_count}",
    f"Failed logins: {failed_count}",
    "",
    "Failed logins by IP:"
]

for ip, count in failed_by_ip.items():
    report_lines.append(f"{ip}: {count}")

report_lines.extend(["", "Suspicious IP alerts:"])

for ip, count in failed_by_ip.items():
    if count >= threshold:
        report_lines.append(
            f"WARNING: {ip} had {count} failed login attempts"
        )

report_text = "\n".join(report_lines)
print(report_text)

with open("reports/analysis_report.txt", "w") as report_file:
    report_file.write(report_text + "\n")

print("\nReport saved to reports/analysis_report.txt")
