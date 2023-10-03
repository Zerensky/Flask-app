import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class TaskBaseAttrs(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[bool] = None


class Task(TaskBaseAttrs):
    id: int


collection = [
    Task(id=1, title='Task_1', description='...1...', status=True),
    Task(id=2, title='Task_2', description='...2...', status=False),
    Task(id=1, title='Task_3', description='...3...', status=False),
    Task(id=2, title='Task_4', description='...4...', status=True),
]


@app.get('/tasks/', response_model=list[Task])
def tasks():
    return collection


@app.get('/tasks/{id}', response_model=Task)
def task(id: int):
    for task in collection:
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post('/tasks/', response_model=Task)
def create_task(attrs: TaskBaseAttrs):
    task = Task(id=len(collection) + 1, **attrs.dict())
    collection.append(task)
    return task


@app.put('/tasks/{id}', response_model=Task)
def update_task(id: int, attrs: TaskBaseAttrs):
    for task in collection:
        if task.id == id:
            task.title = attrs.title
            task.description = attrs.description
            task.status = attrs.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete('/tasks/{id}', response_model=dict)
def destroy_tasks(id: int):
    for task in collection:
        if task.id == id:
            collection.remove(task)
            return {'message': 'Destroy was successfully'}
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
