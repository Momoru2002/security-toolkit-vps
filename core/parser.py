def parse_command(command: str):

    parts = command.strip().split()

    if not parts:
        return None, []

    module = parts[0]
    args = parts[1:]

    return module, args