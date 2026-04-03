import sqlite3

DB_NAME = "database.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_id TEXT PRIMARY KEY,
        title TEXT,
        company TEXT,
        url TEXT,
        description TEXT,
        status TEXT,
        score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def job_exists(job_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM jobs WHERE job_id=?", (job_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None

def insert_job(job):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO jobs (job_id, title, company, url, description, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        job["job_id"],
        job["title"],
        job["company"],
        job["url"],
        job["description"],
        "NEW"
    ))

    conn.commit()
    conn.close()
