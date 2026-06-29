import os
from pathlib import Path
from rich.prompt import Confirm
from rich.console import Console

console = Console()

# পূর্বের পাথ হেল্পার ক্লাস
class PathHelper:
    @staticmethod
    def get_cwd() -> Path:
        return Path(os.getcwd())

    @staticmethod
    def get_script_dir() -> Path:
        return Path(__file__).resolve().parent

    @staticmethod
    def get_template_dir() -> Path:
        root_dir = PathHelper.get_script_dir().parent
        return root_dir / "cmd"

# মূল ফাংশন
def write_from_template(template_name: str, output_relative_path: str, context: dict = None):
    """
    template_name: 'model.txt'
    output_relative_path: 'app/user/model.py'
    """
    # ১. টেমপ্লেট এবং আউটপুট ফাইলের ফুল পাথ তৈরি করা
    template_path = PathHelper.get_template_dir() / template_name
    output_path = PathHelper.get_cwd() / output_relative_path

    # ২. ফাইল আগে থেকে থাকলে ওভাররাইট (Overwrite) ওয়ার্নিং
    if output_path.exists():
        console.print(f"[bold yellow]⚠ Warning: File '{output_relative_path}' already exists![/bold yellow]")
        overwrite = Confirm.ask("Do you want to overwrite it?", default=False)
        if not overwrite:
            console.print("[bold blue]Skip creation.[/bold blue]")
            return

    # ৩. ফাইল তৈরি এবং রাইট করার লজিক
    if template_path.exists():
        content = template_path.read_text(encoding="utf-8")
        
        # ডায়নামিক ভ্যারিয়েবল রিপ্লেস করা (যদি থাকে)
        if context:
            for key, value in context.items():
                content = content.replace(f"{{{{ {key} }}}}", value)
                content = content.replace(f"{{{{{key}}}}}", value)

        # ম্যাজিক লাইন: 'app/user/' ফোল্ডারগুলো না থাকলে এটি অটোমেটিক তৈরি করবে
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # ফাইলটি রাইট করা
        output_path.write_text(content, encoding="utf-8")
        console.print(f"[bold green]✔ Successfully created: {output_relative_path}[/bold green]")
    else:
        console.print(f"[bold red]❌ Error: Template '{template_name}' not found at {template_path}[/bold red]")
