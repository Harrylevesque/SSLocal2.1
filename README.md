# SSLocal2.1 FastAPI

This is a minimal FastAPI-ready project scaffold added to the workspace.

Quick start

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Health check: GET http://localhost:8000/health

5. Example POST: POST http://localhost:8000/echo with JSON {"message": "hello"}

Run tests:

```bash
pytest -q
```

