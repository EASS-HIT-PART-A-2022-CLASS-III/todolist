from fastapi import FastAPI, HTTPException
from model import Todo
from fastapi.middleware.cors import CORSMiddleware

import httpx

from db import(
    fetch_all_todo,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo,
)
# App
app = FastAPI()

origins = ['https://localhost:8000', 'http://localhost:8000']

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_route():
    return {"Send": "Recive"}



@app.get("/api/todo/all", name="trial")
async def get_todo():
    async with httpx.AsyncClient() as client:
        response = await fetch_all_todo()
    return response



@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    async with httpx.AsyncClient() as client:
        response = await fetch_one_todo(client, title)
    if response:
        return response
    raise HTTPException(404, f"Could not find a todo with this title {title}")


@app.post("/api/todo/add", response_model=Todo)
async def post_todo(todo: Todo):
    async with httpx.AsyncClient() as client:
        response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, f"Problem! try again later")


@app.put("/api/todo/update/{title}", response_model=Todo)
async def put_todo(todo: Todo):
    async with httpx.AsyncClient() as client:
        response = await update_todo(todo.dict())
    if response:
        return response
    raise HTTPException(404, f"Could not find a todo with this title {title}")


@app.delete("/api/todo/delete/{title}")
async def delete_todo(title):
    async with httpx.AsyncClient() as client:
        response = await remove_todo(title)
    if response:
        return response
    raise HTTPException(404, f"Could not find a todo with this title {title}")