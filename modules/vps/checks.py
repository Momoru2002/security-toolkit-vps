CHECKS = [

    {
        "id": "VPS-001",
        "category": "SSH",
        "severity": "CRITICAL",
        "score": 9.5,
        "description": "SSH root login enabled",
        "cmd": "sshd -T | grep permitrootlogin",
        "bad_pattern": "yes",
        "fix": "Set PermitRootLogin no"
    },

    {
        "id": "VPS-002",
        "category": "SSH",
        "severity": "HIGH",
        "score": 8.5,
        "description": "Password authentication enabled",
        "cmd": "sshd -T | grep passwordauthentication",
        "bad_pattern": "yes",
        "fix": "Disable password authentication"
    },

]