from pathlib import Path
from karigor.helper.path_helper import PathHelper
from rich.console import Console

console = Console()

def append_model_to_migrations(module_name: str, model_name: str):
    # Target file where Alembic or SQLAlchemy imports everything to discover tables
    file_path = PathHelper.get_cwd() / "database" / "migrations" / "base.py"
    
    new_import = f"from app.modules.{module_name}.{module_name}_model import {model_name}"
    # This exposes the model to your migration metadata registry __all__ proxy list
    new_all_entry = f"    \"{model_name}\","

    # 1. Handle File Generation if it doesn't exist
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        base_content = (
            "from database.database import Base  # Your SQLAlchemy Declarative Base\n"
            f"{new_import}\n\n"
            "__all__ = [\n"
            f"{new_all_entry}\n"
            "]\n"
        )
        file_path.write_text(base_content, encoding="utf-8")
        console.print(f"[bold green]✔ Created base.py and registered {model_name}[/bold green]")
        return

    content = file_path.read_text(encoding="utf-8")

    # 2. Prevent Duplicate Imports
    if new_import in content:
        console.print(f"[bold yellow]⏭ Model '{model_name}' already registered in migrations/base.py[/bold yellow]")
        return

    lines = content.splitlines()
    
    # 3. Locate positions for clean appending
    import_index = 0
    all_block_index = -1

    for i, line in enumerate(lines):
        if line.startswith("from ") or line.startswith("import "):
            import_index = i + 1 
        if "__all__ = [" in line:
            all_block_index = i

    # Insert the import statement into the top imports cluster
    lines.insert(import_index, new_import)
    
    # Adjust tracking index by 1 since we just pushed a new row above it
    if all_block_index != -1:
        all_block_index += 1
        # Insert the string entry directly inside the array block opening
        lines.insert(all_block_index + 1, new_all_entry)
    else:
        # Fallback if structural __all__ block template wasn't found
        lines.append("\n__all__ = [")
        lines.append(new_all_entry)
        lines.append("]")

    # 4. Save and Format 
    file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    console.print(f"[bold green]✔ Registered {model_name} model inside migrations/base.py[/bold green]")

# Execution Example:
# append_model_to_migrations(module_name="user", model_name="User")
