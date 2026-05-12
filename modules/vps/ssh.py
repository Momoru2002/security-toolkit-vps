"""
modules/vps/ssh.py
SSH utilities
"""

import paramiko


def create_ssh_client(
    host,
    username,
    password=None,
    key_path=None,
    port=22
):

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(
        paramiko.AutoAddPolicy()
    )

    if key_path:

        client.connect(
            hostname=host,
            username=username,
            key_filename=key_path,
            port=port,
            timeout=10
        )

    else:

        client.connect(
            hostname=host,
            username=username,
            password=password,
            port=port,
            timeout=10
        )

    return client


def run_command(client, command):

    try:

        stdin, stdout, stderr = client.exec_command(
            command,
            timeout=10
        )

        output = stdout.read().decode().strip()

        if not output:

            output = stderr.read().decode().strip()

        return output

    except Exception as error:

        return f"ERROR: {error}"