from db import init_db
from app.job_fetcher import fetch_jobs
from rich import print

def main():
    print("[bold green]🚀 Career Agent Running Day 2...[/bold green]")

    init_db()

    new_jobs = fetch_jobs()

    print(f"[bold blue]📦 Jobs stored: {new_jobs}[/bold blue]")
    print("[bold yellow]➡️ Ready for Day 3 (AI Scoring)[/bold yellow]")

if __name__ == "__main__":
    main()
