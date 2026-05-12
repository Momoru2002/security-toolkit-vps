"""
core/router.py
Main command router
"""

from rich.console import Console
from rich.panel import Panel

from modules.vps.main import run as vps_run
from modules.ports.main import run as ports_run
from modules.ssl.main import run as ssl_run
from modules.logs.main import run as logs_run
from modules.ai.main import run as ai_run

console = Console()

ROUTES = {
    "vps": {
        "handler": vps_run,
        "description": "VPS security audit"
    },

    "ports": {
        "handler": ports_run,
        "description": "Port scanner"
    },

    "ssl": {
        "handler": ssl_run,
        "description": "SSL/TLS analyzer"
    },

    "logs": {
        "handler": logs_run,
        "description": "Log analyzer"
    },

    "ai": {
        "handler": ai_run,
        "description": "AI threat analyzer"
    },
}


def show_help():

    console.print()

    console.print(Panel.fit(
        "[bold cyan]MOMORU Offensive Framework[/bold cyan]\n"
        "[dim]Interactive Security CLI[/dim]",
        border_style="cyan"
    ))

    console.print("[bold yellow]Available Commands:[/bold yellow]\n")

    console.print("  [green]vps <host> <user>[/green]")
    console.print("      Audit VPS via SSH")
    console.print()

    console.print("  [green]ports <host>[/green]")
    console.print("      Scan open ports")
    console.print()

    console.print("  [green]ssl <host>[/green]")
    console.print("      Analyze SSL/TLS")
    console.print()

    console.print("  [green]logs <file>[/green]")
    console.print("      Analyze log file")
    console.print()

    console.print("  [green]ai <text>[/green]")
    console.print("      AI security analysis")
    console.print()

    console.print("  [green]help[/green]")
    console.print("      Show this help")
    console.print()

    console.print("  [green]exit[/green]")
    console.print("      Exit framework")
    console.print()


def execute(module: str, args: list):

    module = module.lower().strip()

    # =========================
    # HELP
    # =========================

    if module in ["help", "?"]:
        show_help()
        return

    # =========================
    # CHECK MODULE
    # =========================

    route = ROUTES.get(module)

    if not route:

        console.print(
            f"[red][ERROR][/red] Unknown module: {module}"
        )

        return

    handler = route["handler"]

    try:

        handler(args)

    except KeyboardInterrupt:

        console.print(
            "\n[yellow][!] Interrupted by user[/yellow]"
        )

    except Exception as error:

        console.print(
            f"[red][CRITICAL][/red] {error}"
        )