import os
import subprocess

def init_cmd(console):
    """Initialize a Feature-driven / Modular folder structure with main.py"""
    initial_packages = ["fastapi", "uvicorn[standard]", "pydantic-settings", "sqlalchemy"]
    console.print("[yellow]⏳ Installing core packages...[/yellow]")
    subprocess.run(["pip", "install"] + initial_packages, check=True)

    folders = [
        "app", 
        "routes", 
        "config", 
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        init_file = os.path.join(folder, "__init__.py")
        with open(init_file, "w") as f:
            pass 

    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, "templates")

    def write_from_template(template_name, output_path):
        template_path = os.path.join(template_dir, template_name)

        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as t_file:
                content = t_file.read()
            with open(output_path, "w", encoding="utf-8") as o_file:
                o_file.write(content)
        else:
            console.print(f"[bold red]❌ Error: Template file '{template_name}' not found at {template_path}![/bold red]")
    
    write_from_template("migrations_base.txt", "database/migrations/base.py")
    write_from_template("env_setting_template.txt", "config/env_setting.py")
    write_from_template("meta_data_template.txt", "config/meta_data.py")
    write_from_template("env_example.txt", ".env.example")
    write_from_template("main_template.txt", "main.py")
    write_from_template("env_example.txt", ".env")

    console.print("[bold green]✔[/bold green] Success: Modular folder structure, main.py, config/env_setting.py, and database/migrations/base.py created!")
