"""Painéis estilizados com Rich para dashboard interativo do DevBox.

Layout baseado no protótipo (IDEAS | REACT | SPRING BOOT),
com foco em clareza e navegação intuitiva.
"""

from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from rich.text import Text
from rich import box



console = Console()

# =====================================================
# FUNÇÕES DE ESTILO / COMPONENTES
# =====================================================

def _make_ide_panel(focused: bool = False) -> Panel:
    """Painel das IDEs com links diretos de download."""
    content = Text()
    content.append("[1] VS Code\n", style="bold cyan")
    content.append("[2] Vim / Neovim\n", style="bold cyan")
    content.append("[3] Visual Studio\n", style="bold cyan")
    content.append("[4] IntelliJ IDEA\n", style="bold cyan")
    content.append("\n[dim]Selecione uma IDE para abrir o link de download[/]")
    return Panel(
        Align.center(content),
        title="[bold]IDEAS[/]",
        border_style="bright_white" if focused else "grey50",
        box=box.HEAVY if focused else box.ROUNDED,
        padding=(1, 2)
    )


def _make_react_panel(focused: bool = False) -> Panel:
    """Painel React — criação e setup rápido de projetos."""
    content = Text()
    content.append("[1] Criar projeto rápido\n", style="bold green")
    content.append("[2] Adicionar libs essenciais\n", style="bold green")
    content.append("[3] Configurar TypeScript\n", style="bold green")
    content.append("\n[dim]Automatiza o processo React padrão[/]")
    return Panel(
        Align.center(content),
        title="[bold]REACT[/]",
        border_style="bright_white" if focused else "grey50",
        box=box.HEAVY if focused else box.ROUNDED,
        padding=(1, 2)
    )


def _make_spring_panel(focused: bool = False) -> Panel:
    """Painel Spring Boot — configuração simplificada."""
    content = Text()
    content.append("[1] Criar projeto Spring Boot\n", style="bold blue")
    content.append("[2] Adicionar dependência\n", style="bold blue")
    content.append("[3] Configurar Banco de Dados\n", style="bold blue")
    content.append("\n[dim]Baseado no Spring Initializr[/]")
    return Panel(
        Align.center(content),
        title="[bold]SPRING BOOT[/]",
        border_style="bright_white" if focused else "grey50",
        box=box.HEAVY if focused else box.ROUNDED,
        padding=(1, 2)
    )


def _make_center_boxes(focused_idx: int = -1) -> Columns:
    """Cria as 3 colunas centrais alinhadas, como no layout do Figma."""
    panels = [
        _make_ide_panel(focused_idx == 0),
        _make_react_panel(focused_idx == 1),
        _make_spring_panel(focused_idx == 2)
    ]
    return Columns(panels, expand=True, equal=True, align="center")



BANNERS = {
     "small": r"""
  ██████╗ ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗
  ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔═══██╗╚██╗██╔╝
  ██║  ██║█████╗  ██║   ██║██████╔╝██║   ██║ ╚███╔╝
  ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══██╗██║   ██║ ██╔██╗
  ██████╔╝███████╗ ╚████╔╝ ██████╔╝╚██████╔╝██╔╝ ██╗
  ╚═════╝ ╚══════╝  ╚═══╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
""",
}

# =====================================================
# VISUALIZAÇÃO PRINCIPAL
# =====================================================s
def get_banner(name: str = "small") -> str:
    """Retorna o banner ASCII do DevBox."""
    return BANNERS.get(name, BANNERS["small"])


# =====================================================
# LOOP PRINCIPAL
# =====================================================
