from db import init_db
from rich import print

def main():
    print("[bold green]🚀 Career Agent Starting...[/bold green]")
    
    init_db()
    
    print("[bold blue]✅ Database initialized[/bold blue]")
    print("[bold yellow]🧠 System ready for Day 2 (Job Fetching)[/bold yellow]")

if __name__ == "__main__":
    main()
