import os
import re
from datetime import datetime

def analyze_enterprise_server_logs(input_filename="server_logs.txt", output_filename="incident_report.txt"):
    if not os.path.exists(input_filename):
        print(f"Error: {input_filename} target log space not found.")
        return
    critical_count = 0
    error_count = 0
    warning_count = 0
    incident_pool = []
    log_pattern = re.compile(r"^\[(?P<timestamp>.*?)\] \[(?P<level>.*?)\] \[(?P<component>.*?)\] \[(?P<req_id>.*?)\] - (?P<message>.*)$")
    with open(input_filename, "r", encoding="utf-8") as infile:
        for line in infile:
            match = log_pattern.match(line.strip())
            if match:
                data = match.groupdict()
                level = data["level"]
                if level == "CRITICAL":
                    critical_count += 1
                    incident_pool.append(data)
                elif level == "ERROR":
                    error_count += 1
                    incident_pool.append(data)
                elif level == "WARNING":
                    warning_count += 1
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write("==================================================\n")
        outfile.write("        ENTERPRISE INCIDENT ANALYTICS REPORT      \n")
        outfile.write("==================================================\n")
        outfile.write(f"Generated On : {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
        outfile.write(f"Target Source: {input_filename}\n")
        outfile.write("--------------------------------------------------\n")
        outfile.write("📊 EXECUTIVE SUMMARY (TOTAL METRICS):\n")
        outfile.write(f"  [CRITICAL CHANNELS] : {critical_count} incidents detected.\n")
        outfile.write(f"  [ERROR BREAKDOWNS] : {error_count} system faults.\n")
        outfile.write(f"  [WARNING ALERTS]   : {warning_count} performance anomalies.\n")
        outfile.write("--------------------------------------------------\n\n")
        outfile.write("🚨 DETAILED INCIDENT LOG SHEET (CRITICAL & ERROR):\n")
        outfile.write("--------------------------------------------------\n")
        if not incident_pool:
            outfile.write("Zero threat vectors detected. System operation stable.\n")
        else:
            for incident in incident_pool:
                report_line = f"[{incident['timestamp']}] [{incident['level']}] [{incident['component']}] -> {incident['message']}\n"
                outfile.write(report_line)
        outfile.write("==================================================\n")
        outfile.write("               END OF EXECUTIVE REPORT            \n")
        outfile.write("==================================================\n")

if __name__ == "__main__":
    analyze_enterprise_server_logs()
