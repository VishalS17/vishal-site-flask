
import sqlite3
from pathlib import Path
from typing import List, Dict, Optional, Tuple

DB_PATH = Path(__file__).parent / "projects.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                imagefilename TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()

def list_projects() -> List[sqlite3.Row]:
    init_db()
    with get_connection() as conn:
        cur = conn.execute("SELECT id, title, description, imagefilename, created_at FROM projects ORDER BY created_at DESC, id DESC")
        return cur.fetchall()

def insert_project(title: str, description: str, imagefilename: str) -> int:
    init_db()
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO projects (title, description, imagefilename) VALUES (?, ?, ?)",
            (title.strip(), description.strip(), imagefilename.strip()),
        )
        conn.commit()
        return cur.lastrowid
