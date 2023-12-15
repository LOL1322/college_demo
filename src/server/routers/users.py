from fastapi import APIRouter
from src.server.resolvers import users
from src.server.database.models import Users

rout = APIRouter(prefix='/users', tags=["Users"])


@rout.get(path='/get/{userID}', response_model=dict)
def get_user(userID: int) -> dict:
    return users.get(userID=userID)


@rout.get(path='/get', response_model=dict)
def get_all_users() -> dict:
    return users.get_all()


@rout.post(path='/new', response_model=dict)
def new_user(data: Users) -> dict:
    return users.new(data=data)


@rout.put(path='/update/{userID}', response_model=dict)
def update_user(data: Users, userID: int) -> dict:
    return users.update(userID=userID, new_data=data)


@rout.delete(path='/delete/{userID}', response_model=dict)
def delete_user(userID: int) -> dict:
    return users.delete(userID=userID)