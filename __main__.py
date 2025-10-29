from rich.console import Console
from rich.prompt import Prompt
from src.ui.panels import get_banner

console = Console()

def show_menu():
    # Mostra o banner no topo
    banner = get_banner("small")
    console.print(banner, style="bold magenta")
    console.rule("[bold magenta]DevBox Search[/bold magenta]")

    while True:
        registry = Prompt.ask(
            "[bold yellow]Choose registry[/bold yellow]",
            choices=["npm", "pypi", "q"],
            default="npm"
        )

        if registry == "q":
            console.print("[bold red]Goodbye![/] 👋")
            break

        dep = Prompt.ask("[bold cyan]Enter dependency name[/]")
        if not dep.strip():
            console.print("[bold red]Please enter a valid dependency name.[/]")
            continue

        console.print(f"\n[bold cyan]Searching for dependency:[/] {dep}...\n")

        if registry == "npm":
            search_npm(dep)
        else:
            search_pypi(dep)

        console.print("")  # linha em branco entre buscas


if __name__ == "__main__":
    show_menu()
