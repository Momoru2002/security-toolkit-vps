"""
modules/ai/analyzer.py
Enhanced AI threat analyzer with severity levels
"""

SUSPICIOUS_KEYWORDS = {
    # CRITICAL
    "reverse shell":     "CRITICAL",
    "/etc/passwd":       "CRITICAL",
    "/etc/shadow":       "CRITICAL",
    "union select":      "CRITICAL",
    "drop table":        "CRITICAL",
    "cmd.exe":           "CRITICAL",
    "../../../":         "CRITICAL",

    # HIGH
    "failed password":   "HIGH",
    "brute":             "HIGH",
    "exploit":           "HIGH",
    "payload":           "HIGH",
    "inject":            "HIGH",
    "unauthorized":      "HIGH",
    "malware":           "HIGH",
    "/wp-admin":         "HIGH",
    "/admin/config":     "HIGH",

    # MEDIUM
    "failed":            "MEDIUM",
    "attack":            "MEDIUM",
    "error":             "MEDIUM",
    "denied":            "MEDIUM",
    "blocked":           "MEDIUM",
    "scan":              "MEDIUM",

    # LOW
    "warning":           "LOW",
    "timeout":           "LOW",
    "retry":             "LOW",
}

SEVERITY_ORDER = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}

SEVERITY_COLOR = {
    "CRITICAL": "red",
    "HIGH":     "orange3",
    "MEDIUM":   "yellow",
    "LOW":      "green",
}


def analyze_text(text: str) -> list:
    findings = []
    lower = text.lower()
    seen = set()

    for keyword, severity in SUSPICIOUS_KEYWORDS.items():
        if keyword in lower and keyword not in seen:
            seen.add(keyword)
            findings.append({
                "keyword": keyword,
                "severity": severity,
                "color": SEVERITY_COLOR[severity],
            })

    # Urutkan dari severity tertinggi
    findings.sort(
        key=lambda x: SEVERITY_ORDER[x["severity"]],
        reverse=True
    )

    return findings


def get_overall_severity(findings: list) -> str:
    if not findings:
        return "CLEAN"
    return findings[0]["severity"]