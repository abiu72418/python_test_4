from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.post('/todos/', response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get('/todos/', response_model=List[Todo])
async def get_todos():
    return todos

@app.put('/todos/{todo_id}', response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = todo
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')

@app.delete('/todos/{todo_id}', response_model=Todo)
async def delete_todo(todo_id: int):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            return todos.pop(index)
    raise HTTPException(status_code=404, detail='Todo not found')
