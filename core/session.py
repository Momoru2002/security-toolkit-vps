SESSION = {
    "workspace": "default",
    "target": None,
    "history": []
}


def set_target(target):
    SESSION["target"] = target


def get_target():
    return SESSION["target"]


def add_history(command):
    SESSION["history"].append(command)