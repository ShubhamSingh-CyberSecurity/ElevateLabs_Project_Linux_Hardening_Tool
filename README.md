 ElevateLabs- Cybersecurity Internship Project
 
 -----------------------Linux Hardening Audit Tool------------------------
 
🛡️ Linux Hardening Audit Tool

A simple Python-based auditing tool for Linux systems (tested on Kali Linux) that checks basic security configurations and generates a score-based report with hardening recommendations.

 Features

This tool performs the following security audits:

-  Checks UFW (firewall) status
-  Verifies SSH configuration (e.g., root login & password auth)
-  Inspects file permissions on sensitive files (`/etc/shadow`, `/etc/passwd`)
-  Lists disabled/unused system services
-  Scans for rootkits (if `chkrootkit` is installed)
-  Calculates a security score out of 5
-  Recommends hardening actions
-  Generates a detailed text report

 Requirements

- Python 3.x
- `ufw` (Uncomplicated Firewall)
- `chkrootkit` (optional, for rootkit check)

Install requirements:

```bash
sudo apt update
sudo apt install ufw chkrootkit -y
