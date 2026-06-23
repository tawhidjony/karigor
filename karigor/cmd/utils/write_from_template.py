import os
from rich.console import Console
console = Console()


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

