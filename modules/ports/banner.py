"""
modules/ports/banners.py
Banner grabbing utilities
"""

import socket


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB",
}


def grab_banner(host: str, port: int, timeout: int = 3):

    try:

        sock = socket.socket()
        sock.settimeout(timeout)

        sock.connect((host, port))

        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        except:
            pass

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if not banner:
            return "Unknown service"

        return banner[:200]

    except Exception:
        return None


def identify_service(port: int):

    return COMMON_PORTS.get(port, "Unknown")