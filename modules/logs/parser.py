"""
modules/logs/parser.py
Advanced Log Security Analyzer
"""

import re
from collections import Counter


SUSPICIOUS_KEYWORDS = [
    "failed",
    "invalid",
    "error",
    "attack",
    "brute",
    "injection",
    "unauthorized",
    "exploit",
    "malware",
    "blocked",
]

WARNING_KEYWORDS = [
    "warning",
    "denied",
    "timeout",
    "refused",
]

INFO_KEYWORDS = [
    "accepted",
    "connected",
    "success",
]


IP_REGEX = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"


def extract_ips(text):

    return re.findall(
        IP_REGEX,
        text
    )


def classify_line(line):

    lower = line.lower()

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in lower:
            return "SUSPICIOUS"

    for keyword in WARNING_KEYWORDS:

        if keyword in lower:
            return "WARNING"

    for keyword in INFO_KEYWORDS:

        if keyword in lower:
            return "INFO"

    return "NORMAL"


def analyze_log_file(path):

    total_lines = 0

    suspicious_count = 0

    warning_count = 0

    info_count = 0

    suspicious_entries = []

    ip_counter = Counter()

    findings = []

    with open(
        path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        for line_number, line in enumerate(file, start=1):

            total_lines += 1

            classification = classify_line(line)

            ips = extract_ips(line)

            for ip in ips:
                ip_counter[ip] += 1

            entry = {
                "line": line_number,
                "type": classification,
                "content": line.strip()[:300],
                "ips": ips,
            }

            if classification == "SUSPICIOUS":

                suspicious_count += 1

                suspicious_entries.append(entry)

            elif classification == "WARNING":

                warning_count += 1

            elif classification == "INFO":

                info_count += 1

    # Detect brute-force attempts
    brute_force_ips = []

    for ip, count in ip_counter.items():

        if count >= 5:

            brute_force_ips.append({
                "ip": ip,
                "attempts": count
            })

            findings.append({
                "severity": "HIGH",
                "type": "Brute Force",
                "detail": f"IP {ip} appears {count} times in logs"
            })

    # General suspicious activity
    if suspicious_count >= 10:

        findings.append({
            "severity": "HIGH",
            "type": "Suspicious Activity Spike",
            "detail": f"{suspicious_count} suspicious log entries detected"
        })

    elif suspicious_count > 0:

        findings.append({
            "severity": "MEDIUM",
            "type": "Suspicious Activity",
            "detail": f"{suspicious_count} suspicious entries found"
        })

    # Calculate risk score
    risk_score = min(
        100,
        suspicious_count * 3 + warning_count
    )

    return {
        "file": path,
        "risk_score": risk_score,
        "total_lines": total_lines,
        "suspicious": suspicious_count,
        "warnings": warning_count,
        "info": info_count,
        "top_ips": ip_counter.most_common(10),
        "brute_force_ips": brute_force_ips,
        "suspicious_entries": suspicious_entries[:20],
        "findings": findings,
    }