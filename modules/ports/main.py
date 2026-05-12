"""
modules/ports/main.py
Port scanning module
"""

from rich.console import Console
from rich.table import Table

from modules.ports.scanner import scan_ports

console = Console()


def run(args):

    if len(args) < 1:

        console.print(
            "[red]Usage:[/red] ports <host>"
        )

        return

    host = args[0]

    console.print(f"\n[cyan]Scanning:[/cyan] {host}\n")

    results = scan_ports(host)

    table = Table()

    table.add_column("Port")
    table.add_column("Status")
    table.add_column("Service")

    for result in results:

        table.add_row(
            str(result["port"]),
            result["status"],
            result["service"]
        )

    console.print(table)