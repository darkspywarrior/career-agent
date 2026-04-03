import requests
from db import insert_job, job_exists

API_URL = "https://www.arbeitnow.com/api/job-board-api"

def fetch_jobs():
    print("🌐 Fetching jobs...")

    response = requests.get(API_URL)
    data = response.json()

    jobs = data.get("data", [])
    new_jobs = 0

    for job in jobs[:40]:
        job_id = job.get("slug")

        if job_exists(job_id):
            continue

        job_data = {
            "job_id": job_id,
            "title": job.get("title"),
            "company": job.get("company_name"),
            "url": job.get("url"),
            "description": job.get("description")
        }

        insert_job(job_data)
        new_jobs += 1

    print(f"✅ Added {new_jobs} new jobs")

    return new_jobs
