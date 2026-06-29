from karigor.helper.path_helper import PathHelper
from rich.console import Console

console = Console()

def register_route_in_api_file(module_name: str, class_name: str):
    api_file_path = PathHelper.get_cwd() / "routes" / "api.py"
    
    # নতুন যে মডিউলটি তৈরি হচ্ছে, তার ইম্পোর্ট এবং রাউটার লাইন
    new_import = f"from app.modules.{module_name}.{module_name}_route import router as {module_name}_router"
    new_include = f"v1_router.include_router({module_name}_router)"

    # ১. যদি ফাইলটি আগে থেকে না থাকে, তবে একটি ডিফল্ট বেস ফাইল তৈরি করবে
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

    # ২. যদি ফাইলটি আগে থেকে থাকে, তবে সেটিকে রিড করে ডাইনামিকালি আপডেট করবে
    content = api_file_path.read_text(encoding="utf-8")

    # ডুপ্লিকেট এন্ট্রি বন্ধ করতে চেক করা (একই মডিউল যেন দুইবার যোগ না হয়)
    if new_import in content:
        console.print(f"[bold yellow]⏭ Route for '{module_name}' already registered inside routes/api.py[/bold yellow]")
        return

    # ফাইলটিকে লাইনে লাইনে ভাগ করা
    lines = content.splitlines()
    
    import_index = 0
    router_index = -1

    # লাইনের পজিশন খুঁজে বের করার লুপ
    for i, line in enumerate(lines):
        if line.startswith("from ") or line.startswith("import "):
            import_index = i + 1 # সর্বশেষ ইম্পোর্ট লাইনের ঠিক নিচে নতুন ইম্পোর্ট বসবে
        if "v1_router = APIRouter()" in line:
            router_index = i

    # সঠিক পজিশনে নতুন লাইনগুলো পুশ করা
    lines.insert(import_index, new_import)
    
    # ইম্পোর্ট যোগ করার কারণে ইনডেক্স ১ বেড়েছে, তাই router_index এর সাথে রি-অ্যাডজাস্ট করা হলো
    if router_index != -1:
        # ফাইলের একদম শেষে অথবা v1_router ব্লকের নিচে include লাইনটি যোগ করবে
        lines.append(new_include) 
    else:
        # কোনো কারণে v1_router ডিক্লেয়ারেশন না থাকলে নিচে নরমালি ব্যাকআপ হিসেবে যোগ করবে
        lines.append("\nv1_router = APIRouter()")
        lines.append(new_include)

    # সব লাইন জোড়া লাগিয়ে ফাইলে পুনরায় রাইট করা
    api_file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    console.print(f"[bold green]✔ Registered {module_name} route inside routes/api.py[/bold green]")
