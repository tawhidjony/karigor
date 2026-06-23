import os
import subprocess
import questionary
from rich.console import Console
console = Console()

def install_db():
    """Install Alembic, and select database drivers interactively"""
    
    drivers_to_install = questionary.checkbox(
        "Select the database drivers you want to install:",
        choices=[
            questionary.Choice("PostgreSQL (psycopg2-binary)", value="psycopg2-binary", checked=True),
            questionary.Choice("MySQL (pymysql)", value="pymysql", checked=False),
        ]
    ).ask()

    if drivers_to_install is None:
        console.print("[bold yellow]✖ Operation cancelled.[/bold yellow]")
        return

    base_packages = ["alembic"]
    final_packages = base_packages + drivers_to_install
    console.print(f"[bold blue]⏳ Installing packages: {', '.join(final_packages)}...[/bold blue]")

    def write_from_template(template_name, output_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(current_dir, "templates")
        template_path = os.path.join(template_dir, template_name)

        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as t_file:
                content = t_file.read()
            with open(output_path, "w", encoding="utf-8") as o_file:
                o_file.write(content)
        else:
            console.print(f"[bold red]❌ Error: Template file '{template_name}' not found at {template_path}![/bold red]")

    try:
        subprocess.run(["pip", "install"] + final_packages, check=True)
        
        if not os.path.exists("alembic"):
            console.print("[bold blue]⏳ Initializing Alembic...[/bold blue]")
            subprocess.run(["alembic", "init", "alembic"], check=True)
            write_from_template("alembic_env.txt", "alembic/env.py")
            console.print("[bold green]✔[/bold green] Database tools and selected drivers installed successfully!")
        else:
            console.print("[yellow]⚠ Alembic is already initialized.[/yellow]")
            write_from_template("alembic_env.txt", "alembic/env.py")
            console.print("[bold green]✔[/bold green] Selected drivers installed and env.py configurations verified successfully!")
            
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]❌ Installation failed:[/bold red] {e}", err=True)
