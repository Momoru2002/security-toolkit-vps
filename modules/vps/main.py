"""
modules/vps/main.py
Advanced VPS Security Audit Module
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress

from modules.vps.ssh import create_ssh_client
from modules.vps.utils import run_vps_audit

console = Console()


def run(args):

    console.print(
        Panel.fit(
            "[bold red]VPS Security Audit[/bold red]\n"
            "[dim]Advanced SSH-based auditing engine[/dim]",
            border_style="red"
        )
    )

    # =====================================================
    # INTERACTIVE INPUT
    # =====================================================

    if len(args) < 2:

        host = console.input(
            "[cyan]Target Host[/cyan]: "
        )

        username = console.input(
            "[cyan]SSH Username[/cyan]: "
        )

        port = console.input(
            "[cyan]SSH Port[/cyan] [dim](22)[/dim]: "
        )

        password = console.input(
            "[cyan]Password[/cyan] [dim](optional)[/dim]: ",
            password=True
        )

    else:

        host = args[0]

        username = args[1]

        port = 22

        password = ""

    # =====================================================
    # DEFAULTS
    # =====================================================

    if not port:
        port = 22

    port = int(port)

    # =====================================================
    # CONNECT SSH
    # =====================================================

    console.print(
        f"\n[yellow]Connecting to[/yellow] "
        f"{username}@{host}:{port}"
    )

    try:

        client = create_ssh_client(
            host=host,
            username=username,
            password=password,
            port=port
        )

    except Exception as error:

        console.print(
            f"[red]SSH Connection Failed:[/red] {error}"
        )

        return

    console.print(
        "[green]SSH Connected Successfully[/green]\n"
    )

    # =====================================================
    # RUN AUDIT
    # =====================================================

    with Progress() as progress:

        task = progress.add_task(
            "[cyan]Running VPS audit...",
            total=100
        )

        result = run_vps_audit(client)

        progress.update(task, completed=100)

    # =====================================================
    # RESULTS TABLE
    # =====================================================

    table = Table(
        title="VPS Audit Results"
    )

    table.add_column("ID")
    table.add_column("Severity")
    table.add_column("Category")
    table.add_column("Status")
    table.add_column("Description")

    for r in result["results"]:

        status_color = (
            "red"
            if r["status"] == "VULNERABLE"
            else "green"
        )

        severity_color = {
            "CRITICAL": "red",
            "HIGH": "yellow",
            "MEDIUM": "cyan",
            "LOW": "green",
        }.get(r["severity"], "white")

        table.add_row(
            r["id"],
            f"[{severity_color}]{r['severity']}[/{severity_color}]",
            r["category"],
            f"[{status_color}]{r['status']}[/{status_color}]",
            r["description"]
        )

    console.print(table)

    # =====================================================
    # SUMMARY
    # =====================================================

    console.print()

    console.print(
        Panel.fit(
            f"[bold cyan]Security Score:[/bold cyan] "
            f"{result['score']}/100\n\n"
            f"[bold red]Findings:[/bold red] "
            f"{result['total_findings']}\n\n"
            f"[bold green]Checks:[/bold green] "
            f"{result['total_checks']}",
            border_style="cyan",
            title="Audit Summary"
        )
    )

    # =====================================================
    # FINDINGS
    # =====================================================

    if result["findings"]:

        findings_table = Table(
            title="Detected Vulnerabilities"
        )

        findings_table.add_column("ID")
        findings_table.add_column("Severity")
        findings_table.add_column("Fix")

        for finding in result["findings"]:

            findings_table.add_row(
                finding["id"],
                finding["severity"],
                finding["fix"]
            )

        console.print(findings_table)

    # =====================================================
    # CLOSE SSH
    # =====================================================

    client.close()

    console.print(
        "\n[green]Audit completed successfully[/green]"
    )