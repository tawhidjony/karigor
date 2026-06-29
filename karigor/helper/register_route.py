from karigor.helper.path_helper import PathHelper
from rich.console import Console

console = Console()

def register_route_in_api_file(module_name: str, class_name: str):
    api_file_path = PathHelper.get_cwd() / "routes" / "api.py"
    new_import = f"from app.modules.{module_name}.{module_name}_route import router as {module_name}_router"
    new_include = f"v1_router.include_router({module_name}_router)"

    if not api_file_path.exists():
        api_file_path.parent.mkdir(parents=True, exist_ok=True)
        base_content = (
            "from fastapi import APIRouter\n\n"
            f"{new_import}\n\n"
            "v1_router = APIRouter()\n\n"
            f"{new_include}\n"
        )
        api_file_path.write_text(base_content, encoding="utf-8")
        console.print(f"[bold green]✔ Created and registered route inside routes/api.py[/bold green]")
        return

    content = api_file_path.read_text(encoding="utf-8")

    if new_import in content:
        console.print(f"[bold yellow]⏭ Route for '{module_name}' already registered inside routes/api.py[/bold yellow]")
        return

    lines = content.splitlines()
    
    import_index = 0
    router_index = -1

    for i, line in enumerate(lines):
        if line.startswith("from ") or line.startswith("import "):
            import_index = i + 1 
        if "v1_router = APIRouter()" in line:
            router_index = i

    lines.insert(import_index, new_import)
    
    if router_index != -1:
        lines.append(new_include) 
    else:
        lines.append("\nv1_router = APIRouter()")
        lines.append(new_include)

    api_file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    console.print(f"[bold green]✔ Registered {module_name} route inside routes/api.py[/bold green]")
