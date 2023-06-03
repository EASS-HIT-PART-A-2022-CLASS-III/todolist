import pytest
from fastapi.testclient import TestClient
import json
from main import app
from model import Todo

from main import(
    get_todo,
    get_todo_by_id,
    post_todo,
    put_todo,
    delete_todo
)

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client




@pytest.mark.asyncio
async def test_create_todo(test_app):
    todo_data = {"title": "Check", "description": "New Todo"}
    todo = Todo(**todo_data)

    response = test_app.post("/api/todo/add", json=todo.dict())
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["title"] == todo_data["title"]
    assert response_data["description"] == todo_data["description"]


