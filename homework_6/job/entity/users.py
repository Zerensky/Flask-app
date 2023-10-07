from fastapi import APIRouter
from db.db import products, database
from typing import List
from models.models import User, UserIn

router = APIRouter()


@router.get("/users/", response_model=List[User])
async def read_users():
    query = products.select()
    return await database.fetch_all(query)


@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = products.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = products.select().where(products.c.id == user_id)
    return await database.fetch_one(query)


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = products.update().where(products.c.id == user_id).values(
        **new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = products.delete().where(products.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}