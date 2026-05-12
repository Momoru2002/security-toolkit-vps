from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from modules.vps.checks import CHECKS
from modules.vps.ssh import run_command


def evaluate_check(check, output):

    if output == "TIMEOUT":
        return False, "Command timeout"

    output = output.strip()

    if check.get("nonempty_is_bad"):

        vulnerable = len(output) > 0

        return vulnerable, output[:150]

    bad_pattern = check.get("bad_pattern")

    if bad_pattern:

        vulnerable = bad_pattern.lower() in output.lower()

        return vulnerable, output[:150]

    return False, output[:150]


def run_single_check(client, check):

    try:

        output = run_command(
            client,
            check["cmd"]
        )

    except Exception:

        output = "TIMEOUT"

    vulnerable, detail = evaluate_check(
        check,
        output
    )

    result = {
        "id": check["id"],
        "category": check["category"],
        "severity": check["severity"],
        "score": check["score"],
        "description": check["description"],
        "status": "VULNERABLE" if vulnerable else "SAFE",
        "detail": detail,
        "fix": check["fix"],
    }

    finding = None

    if vulnerable:

        finding = {
            "module": "vps",
            "id": check["id"],
            "severity": check["severity"],
            "score": check["score"],
            "category": check["category"],
            "description": check["description"],
            "detail": detail,
            "fix": check["fix"],
            "timestamp": datetime.utcnow().isoformat()
        }

    return result, finding


def calculate_security_score(findings):

    penalty = sum(
        finding["score"]
        for finding in findings
    )

    score = max(
        0,
        100 - int(penalty)
    )

    return score


def run_vps_audit(client, threads=10):

    results = []

    findings = []

    with ThreadPoolExecutor(
        max_workers=threads
    ) as executor:

        futures = [

            executor.submit(
                run_single_check,
                client,
                check
            )

            for check in CHECKS
        ]

        for future in as_completed(futures):

            result, finding = future.result()

            results.append(result)

            if finding:

                findings.append(finding)

    results = sorted(
        results,
        key=lambda x: x["id"]
    )

    score = calculate_security_score(
        findings
    )

    return {
        "score": score,
        "results": results,
        "findings": findings,
        "total_checks": len(results),
        "total_findings": len(findings),
    }