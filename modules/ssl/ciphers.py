"""
modules/ssl/ciphers.py
Cipher classification database
"""

WEAK_CIPHERS = [
    "RC4",
    "DES",
    "3DES",
    "MD5",
    "NULL",
    "EXPORT",
    "RC2",
    "IDEA",
]

MEDIUM_CIPHERS = [
    "AES128-SHA",
    "AES256-SHA",
]

STRONG_CIPHERS = [
    "AES256-GCM",
    "AES128-GCM",
    "CHACHA20",
    "ECDHE",
]


def classify_cipher(cipher_name: str):

    if not cipher_name:
        return "UNKNOWN"

    upper = cipher_name.upper()

    for weak in WEAK_CIPHERS:
        if weak in upper:
            return "WEAK"

    for medium in MEDIUM_CIPHERS:
        if medium in upper:
            return "MEDIUM"

    for strong in STRONG_CIPHERS:
        if strong in upper:
            return "STRONG"

    return "UNKNOWN"