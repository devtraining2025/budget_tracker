# Budget Tracker (Python)

A small Python project to demonstrate *developer work* (API + CLI + DB + tests). This repo intentionally excludes any DevOps configuration so you can focus on code, tests, and docs.

## Project ideas

- **Sample idea (bigger): Personal Finance Manager** — multi-user web app with budgets, recurring transactions, import/export, visualizations, and role-based access.
- **Small idea (implemented here): Budget Tracker** — single-user service that supports adding transactions, listing them, and computing monthly summaries. Includes:
  - REST API (FastAPI)
  - Small SQLite-backed DB layer
  - CLI (Click)
  - Unit tests (pytest)

---

## How to run (developer steps)

1. Create a virtualenv and install deps:

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

2. Run the API:

```bash
uvicorn budget_tracker.main:app --reload
```

3. CLI usage (from repo root):

```bash
python -m budget_tracker.cli add --amount 12.5 --date 2025-12-26 --category groceries --description "milk"
python -m budget_tracker.cli summary --year 2025 --month 12
```

4. Run tests:

```bash
pytest -q
```

---

## What I added (developer work)

- `budget_tracker/` package with API, DB, models, CRUD and CLI
- `tests/` with unit tests for DB and API
- `sample_data/transactions.csv` for basic sample imports
- `README.md`, `pyproject.toml`, `requirements.txt`

---

If you want, I can now run the tests here or add a small interactive example or more features (tagging, CSV import/export, paginated endpoints).