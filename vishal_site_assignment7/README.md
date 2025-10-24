# Vishal Site (Flask)

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Run with Docker
```bash
docker build -t vishal-site .
docker run --rm -p 5000:5000 \
  -e FLASK_SECRET_KEY=replace-me \
  vishal-site
```

The app is now available at http://127.0.0.1:5000. A new SQLite database file is created inside the container on first run; mount a host volume if you want to persist it.

## Structure
- app.py
- templates/
- images/
- css/
- js/ (if your original site had it)

> .venv intentionally excluded.
