import os
import subprocess
from datetime import datetime

# Create or overwrite report
with open("audit_report.txt", "w") as report:
    report.write("====================================\n")
    report.write("    LINUX SECURITY AUDIT REPORT     \n")
    report.write("====================================\n")
    report.write(f"Date: {datetime.now()}\n\n")

    # 1. Firewall Status
    report.write("[1] Firewall Status:\n")
    report.write(subprocess.getoutput("ufw status") + "\n")
    report.write(subprocess.getoutput("iptables -L") + "\n\n")

    # 2. SSH Configuration
    report.write("[2] SSH Configuration (PermitRootLogin, PasswordAuthentication):\n")
    report.write(subprocess.getoutput("grep -Ei 'PermitRootLogin|PasswordAuthentication' /etc/ssh/sshd_config") + "\n\n")

    # 3. Sudo Users
    report.write("[3] Sudo Users:\n")
    report.write(subprocess.getoutput("getent group sudo") + "\n\n")

    # 4. World Writable Files
    report.write("[4] World Writable Files (first 10):\n")
    report.write(subprocess.getoutput("find / -type f -perm -o+w 2>/dev/null | head -n 10") + "\n\n")

    # 5. Running Services at Boot
    report.write("[5] Running Services at Boot:\n")
    report.write(subprocess.getoutput("systemctl list-unit-files --state=enabled") + "\n\n")

    # 6. File Permissions
    report.write("[6] /etc/passwd and /etc/shadow Permissions:\n")
    report.write(subprocess.getoutput("ls -l /etc/passwd /etc/shadow") + "\n\n")

    # 7. Rootkit Check (Optional)
    report.write("[7] Rootkit Check (chkrootkit):\n")
    if subprocess.getoutput("which chkrootkit"):
        report.write(subprocess.getoutput("chkrootkit | head -n 10") + "\n\n")
    else:
        report.write("chkrootkit not installed.\n\n")

    report.write("Audit complete ✅. See audit_report.txt\n")

