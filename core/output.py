from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Group
from rich import box

console = Console()


# ─── ASCII Skull (kiri) ────────────────────────────────────────────────────────
_SKULL = """\
[red]  /$$$$$$$$$$$$\\[/red]
[red] /$$$$$$$$$$$$$$\\[/red]
[red]|$$ /$$\\ /$$\\ $$|[/red]
[red]|$$| $$ | $$ |$$|[/red]
[red]|$$\\$$/   \\$$/$$/[/red]
[red]|$$  \\$$$$$$/  $$|[/red]
[red]|$$/  \\$$$$/ \\$$|[/red]
[red] \\$$$$$$$$$$$$$$/ [/red]
[red]  \\$$$$$$$$$$$$/ [/red]
[red]   |$$ | $$ | $$ |[/red]
[red]   |$$_|_$$_|_$$_|[/red]"""

# ─── MOMORU ASCII Title (tengah) ───────────────────────────────────────────────
_TITLE = """\
[bold red]███╗   ███╗ ██████╗ ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗[/bold red]
[bold red]████╗ ████║██╔═══██╗████╗ ████║██╔═══██╗██╔══██╗██║   ██║[/bold red]
[bold red]██╔████╔██║██║   ██║██╔████╔██║██║   ██║██████╔╝██║   ██║[/bold red]
[bold red]██║╚██╔╝██║██║   ██║██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║[/bold red]
[bold red]██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝[/bold red]
[bold red]╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝[/bold red]"""


def _build_center() -> Group:
    title   = Text.from_markup(_TITLE)
    div_top = Text.from_markup("[red]" + "─" * 56 + "[/red]")
    suite   = Text.from_markup("\n[bold red]  RED HAT CYBER SECURITY SUITE[/bold red]\n")
    div_bot = Text.from_markup("[red]" + "─" * 56 + "[/red]")
    tagline = Text.from_markup("\n[bold white]      Secure > Detect > Analyze > Protect[/bold white]\n")

    ver = Table(box=box.SQUARE, show_header=False, border_style="red", padding=(0, 1), expand=False)
    for _ in range(8):
        ver.add_column(no_wrap=True)
    ver.add_row(
        "[bold green]VERSION:[/bold green]",  "[bold white]2.0.0[/bold white]",
        "[bold green]AUTHOR:[/bold green]",   "[bold white]Momoru[/bold white]",
        "[bold green]PLATFORM:[/bold green]", "[bold white]Python 3[/bold white]",
        "[bold green]OS:[/bold green]",       "[bold white]Multi-Platform[/bold white]",
    )

    return Group(title, div_top, suite, div_bot, tagline, ver)


def _build_social() -> Panel:
    t = Table(box=None, show_header=False, padding=(0, 1), expand=False)
    t.add_column(no_wrap=True, width=3)
    t.add_column(no_wrap=True, width=12)
    t.add_column(no_wrap=False, width=28)

    t.add_row("", "", "")
    t.add_row(
        "🐱",
        "[bold white]GitHub[/bold white]",
        "[dim white]https://github.com/Momoru2002[/dim white]",
    )
    t.add_row("", "", "")
    t.add_row(
        "[bold blue]in[/bold blue]",
        "[bold blue]LinkedIn[/bold blue]",
        "[dim white]https://www.linkedin.com/in/\nmuhammad-almas-albirra-\nhamid-3812202b8[/dim white]",
    )
    t.add_row("", "", "")
    t.add_row(
        "[bold magenta]📷[/bold magenta]",
        "[bold magenta]Instagram[/bold magenta]",
        "[dim white]https://www.instagram.com/\nalbirra_19[/dim white]",
    )

    return Panel(
        t,
        title="[bold red]CONNECT WITH ME[/bold red]",
        border_style="red",
        padding=(0, 1),
        width=38,
    )


def banner():
    skull  = Text.from_markup(_SKULL)
    center = _build_center()
    social = _build_social()

    layout = Table.grid(padding=(0, 2), expand=True)
    layout.add_column(width=18, no_wrap=False)
    layout.add_column(ratio=1)
    layout.add_column(width=38, no_wrap=False)
    layout.add_row(skull, center, social)

    console.print(Panel(layout, border_style="red", padding=(1, 2)))


def success(message):
    console.print(f"[green][+][/green] {message}")


def error(message):
    console.print(f"[red][-][/red] {message}")


def info(message):
    console.print(f"[cyan][*][/cyan] {message}")