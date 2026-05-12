"""
modules/ssl/analyzer.py
"""

import ssl
import socket
from datetime import datetime


def analyze_ssl(host: str, port: int = 443):

    context = ssl.create_default_context()

    result = {
        "host": host,
        "port": port,
        "tls_version": "UNKNOWN",
        "cipher": "UNKNOWN",
        "issuer": "UNKNOWN",
        "expires": "UNKNOWN",
        "security": "UNKNOWN"
    }

    try:

        with socket.create_connection((host, port), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=host
            ) as ssock:

                cert = ssock.getpeercert()

                result["tls_version"] = ssock.version()

                cipher = ssock.cipher()

                if cipher:
                    result["cipher"] = cipher[0]

                issuer = cert.get("issuer", [])

                if issuer:
                    result["issuer"] = str(issuer)

                result["expires"] = cert.get(
                    "notAfter",
                    "UNKNOWN"
                )

                weak_versions = [
                    "TLSv1",
                    "TLSv1.1",
                    "SSLv2",
                    "SSLv3"
                ]

                if result["tls_version"] in weak_versions:
                    result["security"] = "WEAK"
                else:
                    result["security"] = "STRONG"

    except Exception as e:

        result["security"] = "ERROR"
        result["error"] = str(e)

    return result