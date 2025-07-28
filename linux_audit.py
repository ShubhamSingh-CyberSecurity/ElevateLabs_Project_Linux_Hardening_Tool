#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

output_file = "linux_audit_report.txt"
report = open(output_file, "w")

report.write("Linux Hardening Audit Report\n")
report.write("Generated on: " + str(datetime.now()) + "\n\n")

score = 0
total_checks = 5
recommendations = []

# 1. Firewall check
report.write("[1] Firewall Status:\n")
ufw_status = subprocess.getoutput("ufw status")
if "active" in ufw_status:
    score += 1
    report.write("✔ UFW is active [PASS]\n")
else:
    report.write("✖ UFW is inactive [FAIL]\n")
    recommendations.append("Enable UFW firewall: `sudo ufw enable`")
report.write(ufw_status + "\n\n")

# 2. SSH Configuration check
report.write("[2] SSH Configuration:\n")
ssh_config = subprocess.getoutput("grep -Ei 'PermitRootLogin|PasswordAuthentication' /etc/ssh/sshd_config")
if "PermitRootLogin no" in ssh_config:
    score += 1
    report.write("✔ PermitRootLogin is disabled [PASS]\n")
else:
    report.write("✖ PermitRootLogin may be enabled [FAIL]\n")
    recommendations.append("Disable root login via SSH: `PermitRootLogin no`")

if "PasswordAuthentication no" in ssh_config:
    score += 1
    report.write("✔ Password authentication is disabled [PASS]\n")
else:
    report.write("✖ Password authentication may be enabled [FAIL]\n")
    recommendations.append("Disable password-based SSH login: `PasswordAuthentication no`")
report.write(ssh_config + "\n\n")

# 3. File permissions check
report.write("[3] File Permissions (/etc/passwd and /etc/shadow):\n")
permissions = subprocess.getoutput("ls -l /etc/passwd /etc/shadow")
report.write(permissions + "\n")
if "-rw-r--r--" in permissions and "----------" in permissions:
    score += 1
    report.write("✔ Permissions are secure [PASS]\n")
else:
    report.write("✖ Permissions may be weak [FAIL]\n")
    recommendations.append("Ensure /etc/shadow is only readable by root.")
report.write("\n")

# 4. Unused services
report.write("[4] Disabled Services (potentially unused):\n")
disabled_services = subprocess.getoutput("systemctl list-unit-files --state=disabled")
report.write(disabled_services + "\n")
score += 1

# 5. Rootkit check
report.write("[5] Rootkit Check (chkrootkit):\n")
if subprocess.getoutput("which chkrootkit"):
    rootkit_output = subprocess.getoutput("sudo chkrootkit")
    report.write(rootkit_output + "\n")
    score += 1
else:
    report.write("chkrootkit not installed. Skipping...\n")
    recommendations.append("Install chkrootkit to scan for rootkits.")

# Final summary
report.write("\n==============================\n")
report.write(f"Security Score: {score}/{total_checks}\n")
report.write("==============================\n\n")

report.write(" Recommendations:\n")
if recommendations:
    for rec in recommendations:
        report.write("- " + rec + "\n")
else:
    report.write("System appears well-configured. No major actions needed.\n")

report.close()
print(f" Audit complete. Report saved to {output_file}")
