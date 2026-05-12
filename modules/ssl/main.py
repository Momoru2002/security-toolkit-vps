"""
modules/ssl/main.py
"""

from rich.console import Console
from rich.table import Table

from modules.ssl.analyzer import analyze_ssl

console = Console()


def run(args):

    if len(args) < 1:

        host = console.input(
            "[cyan]Target Host[/cyan]: "
        )

    else:

        host = args[0]

    console.print(
        f"\n[bold cyan]Analyzing SSL:[/bold cyan] {host}\n"
    )

    result = analyze_ssl(host)

    table = Table(
        "Field",
        "Value"
    )

    for key, value in result.items():

        table.add_row(
            str(key),
            str(value)
        )

    console.print(table)