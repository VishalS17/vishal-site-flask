import os, sqlite3
from vishal_site_assignment7 import DAL

def test_database_file_exists():
    assert os.path.exists(DAL.DB_PATH), f"Database not found at {DAL.DB_PATH}"

def test_database_can_connect():
    conn = sqlite3.connect(DAL.DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects';")
    row = cur.fetchone()
    conn.close()
    assert row is not None, "Table 'projects' not found in database"
