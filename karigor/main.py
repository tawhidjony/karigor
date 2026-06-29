import os
import subprocess
import typer
import datetime
from typing import Optional
from rich.console import Console

from karigor.cmd.initials.init_cmd import init_cmd
from karigor.cmd.install_db.install_db import install_db
from karigor.helper.path_helper import write_from_template
from karigor.cmd.migration.migration_create import migration_create
from karigor.cmd.create.modules.modules_create import modules_create



app = typer.Typer(
    no_args_is_help=True,
    help="Karigor CLI - A Laravel Artisan inspired CLI for Python FastAPI",
)

console = Console()
error_console = Console(stderr=True) 

# -------------------------------------------------------------------------
# ১. karigor init
# -------------------------------------------------------------------------
@app.command(name="init", rich_help_panel="FastApi")
def init():
    """To set up a basic, production-ready FastAPI boilerplate"""
    init_cmd(console)


# -------------------------------------------------------------------------
# ২. karigor serve
# -------------------------------------------------------------------------
@app.command(name="serve", rich_help_panel="FastApi")
def serve():
    """Run the project targeting main.py"""
    if os.path.exists("main.py"):
        console.print("[bold blue]🚀 Starting application via Karigor...[/bold blue]")
        subprocess.run(["python", "main.py"])
    else:
        console.print(
            "[bold red]❌ Error:[/bold red] main.py not found! Run 'karigor init' first.",
            err=True,
        )


# -------------------------------------------------------------------------
# ৪. karigor alembic:install 
# -------------------------------------------------------------------------
@app.command(name="alembic:install", rich_help_panel="Alembic")
def db_install():
    """Install Alembic and setup the configuration without any hassle."""
    install_db()


# -------------------------------------------------------------------------
# ৫. karigor migrate
# -------------------------------------------------------------------------
@app.command(name="alembic:migrate", rich_help_panel="Alembic")
def migrate(
      message: Optional[str] = typer.Argument(
        None, help="Migration message/name (Leave empty to auto-generate timestamp)"
    ),
):
    """Run alembic revision autogenerate and upgrade head (message: optional)"""
    if not os.path.exists("alembic"):
        console.print(
            "[bold red]❌ Error:[/bold red] Alembic is not initialized. Please run [yellow]'karigor alembic:install'[/yellow] first.",
            err=True,
        )
        return
    if not message:
        message = f"migration_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}"
    try:
        console.print(f"[bold blue]⏳ Generating migration: '{message}'...[/bold blue]")
        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", message], check=True
        )

        console.print("[bold blue]⏳ Running migration upgrade head...[/bold blue]")
        subprocess.run(["alembic", "upgrade", "head"], check=True)

        console.print("[bold green]✔[/bold green] Migration completed successfully!")
    except subprocess.CalledProcessError as e:
        error_console.print(f"[bold red]❌ Migration failed:[/bold red] {e}", err=True)


# -------------------------------------------------------------------------
# ৩. karigor create:migration
# -------------------------------------------------------------------------
@app.command(name="alembic:create", rich_help_panel="Alembic")
def create_migration(name: str):
    """Create your migration model (exemple: demo_2026_06_24_150713_table.py)"""
    migration_create(name, console)


# -------------------------------------------------------------------------
# ৬ & ৭. karigor create:model & create:controller
# -------------------------------------------------------------------------
@app.command(name="create:modules", rich_help_panel="Create")
def create_modules(
    path: str = typer.Argument(..., help="The name or path of the model to create."),
    all_components: bool = typer.Option(False, "-a", "--all", help="Create all related components.")
):
    """Create a new modules -a --all"""
    if not all_components:
        typer.secho(
            "Error: You must provide the '-a' or '--all' flag to create modules.", 
            fg=typer.colors.RED, 
            bold=True
        )
        raise typer.Exit(code=1) 

    modules_create(path)
   

@app.command(name="create:model", rich_help_panel="Create")
def create_model(path: str):
    """Create a new Model file (e.g., example/example.py)"""
    module_name = path.lower()     
    class_name = path.capitalize()  
    table_name = f"{module_name}s"
    variables = {
        "class_name": class_name,  
        "table_name": table_name    
    }

    write_from_template('create/modules/templates/models.txt', f'app/modules/{path}/{path}_model.py', context=variables)
  

@app.command(name="create:repository", rich_help_panel="Create")
def create_repository(path: str):
    """Create a new repository file (e.g., example/example.py)"""
    module_name = path.lower()     
    class_name = path.capitalize()  
    table_name = f"{module_name}s"
    variables = {
        "repository_name": class_name,  
        "table_name": table_name,  
        "module_name": module_name,  
    }
    write_from_template('create/modules/templates/repository.txt', f'app/modules/{path}/{path}_repository.py', context=variables)

@app.command(name="create:route", rich_help_panel="Create")
def create_route(path: str):
    """Create a new route file (e.g., example/example.py)"""
    write_from_template('create/modules/templates/route.txt', f'app/modules/{path}/{path}_route.py')

@app.command(name="create:schema", rich_help_panel="Create")
def create_schema(path: str):
    """Create a new schemas file (e.g., example/example.py)"""
    module_name = path.lower()     
    class_name = path.capitalize()  
    table_name = f"{module_name}s"
    variables = {
        "schema_name": class_name,  
        "table_name": table_name,  
        "module_name": module_name,  
    }
    write_from_template('create/modules/templates/schemas.txt', f'app/modules/{path}/{path}_schema.py',context=variables)

@app.command(name="create:services", rich_help_panel="Create")
def create_services(path: str):
    """Create a new services file (e.g., example/example.py)"""
    write_from_template('create/modules/templates/services.txt', f'app/modules/{path}/{path}_services.py')

if __name__ == "__main__":
    app()
