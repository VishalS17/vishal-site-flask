# tests/conftest.py
import os, sys, pytest, sqlite3

# Ensure imports resolve from repo root
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from vishal_site_assignment7 import DAL
from vishal_site_assignment7.app import app

@pytest.fixture(scope="session", autouse=True)
def ensure_db():
    """Create the projects table if it's missing so DAL tests pass consistently."""
    os.makedirs(os.path.dirname(DAL.DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DAL.DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Description TEXT,
            ImageFileName TEXT
        )
    """)
    conn.commit()
    conn.close()

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c
