"""DevBox CLI - Busca de dependências no NPM"""
import subprocess
import json
import os
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from src.ui.panels import get_banner  # importa seu banner

console = Console()

CONFIG_FILE = os.path.expanduser("~/.devbox_config.json")


# ========== Funções de configuração ==========
def save_project_dir(path: str):
    data = {"project_dir": path}
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)


def load_project_dir() -> str | None:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return data.get("project_dir")
    return None


def get_project_directory() -> str:
    """Pergunta o caminho do projeto e valida se existe."""
    saved_dir = load_project_dir()
    if saved_dir and os.path.exists(saved_dir):
        use_saved = Prompt.ask(
            f"[bold yellow]Use saved project directory?[/] [cyan]{saved_dir}[/]",
            choices=["y", "n"],
            default="y"
        )
        if use_saved.lower() == "y":
            console.print(f"[green]✅ Using project directory:[/] {saved_dir}\n")
            return saved_dir

    while True:
        project_dir = Prompt.ask("[bold cyan]Enter your project directory (where package.json is)[/]")
        if os.path.exists(project_dir):
            save_project_dir(project_dir)
            console.print(f"[green]✅ Using project directory:[/] {project_dir}\n")
            return project_dir
        else:
            console.print("[bold red]Directory does not exist! Please enter a valid path.[/]")


# ========== Busca no NPM ==========
def search_npm(dependency: str, project_dir: str) -> None:
    """Busca uma dependência no NPM registry e exibe informações básicas."""
    url = f"https://registry.npmjs.org/{dependency.strip()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latest_version = data["dist-tags"]["latest"]
        info = data["versions"][latest_version]
        description = info.get("description", "No description available.")
        author = info.get("author", {}).get("name", "Unknown author")
        homepage = info.get("homepage", "No homepage available")
        install_command = f"npm install {dependency}"

        console.print(
            Panel.fit(
                f"[bold green]{dependency}[/]\n\n"
                f"[yellow]Description:[/] {description}\n"
                f"[cyan]Latest version:[/] {latest_version}\n"
                f"[magenta]Author:[/] {author}\n"
                f"[blue]Homepage:[/] {homepage}\n"
                f"[bold white]Install:[/] [bold green]{install_command}[/]",
                title="📦 NPM Dependency Info",
                border_style="bright_green"
            )
        )

        choice = Prompt.ask(
            "[bold yellow]Do you want to install this package?[/bold yellow]",
            choices=["y", "n"],
            default="n"
        )
        if choice.lower() == "y":
            console.print(f"[bold cyan]Running:[/] {install_command}\n")
            try:
                subprocess.run(install_command, cwd=project_dir, shell=True, check=True)
                console.print(f"[bold green]✅ Package '{dependency}' installed successfully![/]")
            except subprocess.CalledProcessError:
                console.print(f"[bold red]❌ Failed to install '{dependency}'.[/]")
    else:
        console.print(f"[bold red]❌ Dependency '{dependency}' not found on NPM.[/]")


# ========== Menu principal ==========
def show_menu() -> None:
    """Exibe banner + campo de busca de dependências."""
    banner = get_banner("small")
    console.print(banner, style="bold magenta")
    console.rule("[bold magenta]DevBox Search[/bold magenta]")

    project_dir = get_project_directory()

    while True:
        dep = Prompt.ask("[bold cyan]Enter dependency name (or type 'q' to quit)[/]")
        if dep.lower() in ("q", "quit", "exit"):
            console.print("[bold red]Goodbye![/] 👋")
            break

        console.print(f"\n[bold cyan]Searching for dependency:[/] {dep}...\n")
        search_npm(dep, project_dir)
        console.print("")  # Linha em branco pra separar buscas


if __name__ == "__main__":
    show_menu()
