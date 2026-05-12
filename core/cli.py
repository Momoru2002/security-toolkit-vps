"""
core/cli.py
Interactive shell
"""

from rich.console import Console

from core.router import execute
from core.output import banner

console = Console()


def start_cli():

    # tampilkan banner framework
    banner()

    while True:

        try:

            raw = console.input(
                "\n[bold red]MOMORU >:[/bold red] "
            ).strip()

            # skip kosong
            if not raw:
                continue

            # exit commands
            if raw.lower() in [
                "exit",
                "quit"
            ]:

                console.print(
                    "\n[bold green]Goodbye.[/bold green]"
                )

                break

            # parsing command
            parts = raw.split()

            module = parts[0]
            args = parts[1:]

            # execute module
            execute(module, args)

        except KeyboardInterrupt:

            console.print(
                "\n[yellow]Interrupted by user[/yellow]"
            )

            break

        except Exception as e:

            console.print(
                f"\n[bold red][CRITICAL][/bold red] {e}"
            )