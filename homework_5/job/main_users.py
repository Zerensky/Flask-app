import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class UserBaseAttrs(BaseModel):
    name: str
    surname: str
    age: Optional[int] = None


class User(UserBaseAttrs):
    id: int


collection = [
    User(id=1, name='Ivan', surname='Petrov', age=23),
    User(id=2, name='Roman', surname='Ivanov', age=24),
    User(id=3, name='Jon', surname='Sidorov', age=21),
    User(id=4, name='Sara', surname='Bobrova'),
]


@app.get("/")
async def home():
    return {"Home": "Home"}


@app.get('/users/')
def users():
    return collection


@app.get('/users/{id}')
def user(id: int):
    for user in collection:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post('/users/')
def create_user(attrs: UserBaseAttrs):
    user = User(id=len(collection) + 1, **attrs.dict())
    collection.append(user)
    return user


@app.put('/users/{id}')
def update_user(id: int, attrs: UserBaseAttrs):
    for user in collection:
        if user.id == id:
            user.name = attrs.name
            user.surname = attrs.surname
            user.age = attrs.age
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/users/{id}')
def destroy_users(id: int):
    for user in collection:
        if user.id == id:
            collection.remove(user)
            return {'message': 'Destroy was successfully'}
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    uvicorn.run("main_users:app", host="127.0.0.1", port=8000, reload=True)
