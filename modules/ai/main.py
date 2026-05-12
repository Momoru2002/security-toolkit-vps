"""
modules/ai/main.py
AI security analysis - Enhanced
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from modules.ai.analyzer import analyze_text, get_overall_severity

console = Console()


def run(args):
    if len(args) < 1:
        console.print("[red]Usage:[/red] ai <text>")
        return

    text = " ".join(args)
    findings = analyze_text(text)
    overall = get_overall_severity(findings)

    if not findings:
        console.print(
            Panel("[green]✓ No suspicious indicators detected[/green]",
                  title="AI Threat Analysis")
        )
        return

    # Tabel hasil
    table = Table(title="AI Threat Analysis")
    table.add_column("Keyword", style="cyan")
    table.add_column("Severity", justify="center")

    for f in findings:
        table.add_row(
            f["keyword"],
            f"[{f['color']}]{f['severity']}[/{f['color']}]"
        )

    console.print(table)

    # Overall verdict
    color_map = {
        "CRITICAL": "red",
        "HIGH":     "orange3",
        "MEDIUM":   "yellow",
        "LOW":      "green",
    }
    color = color_map[overall]
    console.print(
        f"\n[bold]Overall Threat Level:[/bold] [{color}]{overall}[/{color}]"
    )