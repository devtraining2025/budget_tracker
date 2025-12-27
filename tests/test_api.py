from fastapi.testclient import TestClient
from budget_tracker.main import app
from budget_tracker.db import DB


def setup_module(module):
    # override app/db with in-memory DB for tests
    app.state.db = DB(":memory:")
    # update module-level crud.db so endpoints use same DB
    import budget_tracker.crud as crud
    crud.db = app.state.db


def test_create_and_get_transactions():
    client = TestClient(app)
    response = client.post("/transactions/", json={"amount": 5.5, "date": "2025-12-25", "category": "food", "description": "test"})
    assert response.status_code == 200
    data = response.json()
    assert abs(data["amount"] - 5.5) < 1e-9

    response = client.get("/transactions/")
    assert response.status_code == 200
    assert len(response.json()) >= 1
