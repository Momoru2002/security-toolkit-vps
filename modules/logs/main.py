"""
modules/logs/main.py
"""

from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from modules.logs.parser import analyze_log_file

console = Console()


def run(args):

    if len(args) < 1:

        path = console.input("[cyan]Log Path[/cyan]: ")

    else:

        path = args[0]

    file_path = Path(path)

    if not file_path.exists():

        console.print(
            f"[bold red]File not found:[/bold red] {path}"
        )
        return

    result = analyze_log_file(path)

    console.print(Panel.fit(
        f"""
[green]Total Lines:[/green] {result['total_lines']}
[green]Suspicious:[/green] {result['suspicious']}
[green]Warnings:[/green] {result['warnings']}
""",
        title="Log Analysis",
        border_style="yellow"
    ))