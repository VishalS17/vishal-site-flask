
import sqlite3
from pathlib import Path
from typing import List, Dict, Optional, Tuple

DB_PATH = Path(__file__).parent / "projects.db"

import os
import sqlite3

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "projects.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Description TEXT,
            ImageFileName TEXT
        )
    """)
    conn.commit()
    conn.close()



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
