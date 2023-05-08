from fastapi import FastAPI, HTTPException
from model import Todo

from db import(
    fetch_all_todo,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo,
)
# App
app = FastAPI()



@app.get("/")
def read_route():
    return {"Ping": "Pong"}


@app.get("/api/todo", name="trial")
async def get_todo():
    response = await fetch_all_todo()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"Could not find a todo with this title {title}")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, f"Something went wrong")


@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title: str, description: str):
    response = await update_todo(title, description)
    if response:
        return response
    raise HTTPException(404, f"Could not find a todo with this title {title}")


@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return response
    raise HTTPException