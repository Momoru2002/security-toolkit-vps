"""
modules/ports/scanner.py
"""

import socket
from concurrent.futures import ThreadPoolExecutor


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT",
}


def scan_port(host, port):

    try:

        sock = socket.socket()

        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        sock.close()

        if result == 0:

            return {
                "port": port,
                "status": "OPEN",
                "service": COMMON_PORTS.get(
                    port,
                    "UNKNOWN"
                )
            }

    except:
        pass

    return None


def scan_ports(host):

    results = []

    ports = list(COMMON_PORTS.keys())

    with ThreadPoolExecutor(max_workers=50) as executor:

        futures = [
            executor.submit(
                scan_port,
                host,
                port
            )
            for port in ports
        ]

        for future in futures:

            result = future.result()

            if result:
                results.append(result)

    return sorted(
        results,
        key=lambda x: x["port"]
    )