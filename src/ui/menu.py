"""DevBox CLI - Busca de dependências no NPM"""
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import requests

console = Console()

def search_npm(dependency: str) -> None:
    """Busca uma dependência no NPM registry e exibe informações básicas."""
    url = f"https://registry.npmjs.org/{dependency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latest_version = data["dist-tags"]["latest"]
        info = data["versions"][latest_version]
        description = info.get("description", "No description available.")
        author = info.get("author", {}).get("name", "Unknown author")
        homepage = info.get("homepage", "No homepage available")

        console.print(
            Panel.fit(
                f"[bold green]{dependency}[/]\n\n"
                f"[yellow]Description:[/] {description}\n"
                f"[cyan]Latest version:[/] {latest_version}\n"
                f"[magenta]Author:[/] {author}\n"
                f"[blue]Homepage:[/] {homepage}",
                title="📦 NPM Dependency Info",
                border_style="bright_green"
            )
        )
    else:
        console.print(f"[bold red]❌ Dependency '{dependency}' not found on NPM.[/]")

def show_menu() -> None:
    """Exibe apenas o campo de busca de dependências."""
    console.rule("[bold magenta]DevBox Search[/bold magenta]")
    while True:
        dep = Prompt.ask("[bold cyan]Enter dependency name (or type 'q' to quit)[/]")
        if dep.lower() in ("q", "quit", "exit"):
            console.print("[bold red]Goodbye![/] 👋")
            break

        console.print(f"[bold cyan]Searching for dependency:[/] {dep}...\n")
        search_npm(dep)
        console.print("")  # Linha em branco pra separar buscas


if __name__ == "__main__":
    show_menu()
