from fastapi import APIRouter
from src.server.resolvers import user
from src.server.database.models import User, UserPass, LoginData

rout = APIRouter(prefix='/user', tags=["Users"])


@rout.get(path='/get/{userID}', response_model=dict)
def get_user(userID: int) -> dict:
    return user.get(userID=userID)


@rout.get(path='/get', response_model=dict)
def get_all_users() -> dict:
    return user.get_all()


@rout.post(path='/new', response_model=dict)
def new_user(data: User) -> dict:
    return user.new(data=data)


@rout.put(path='/update/{userID}', response_model=dict)
def update_user(data: User, userID: int) -> dict:
    return user.update(userID=userID, new_data=data)


@rout.delete(path='/delete/{userID}', response_model=dict)
def delete_user(userID: int) -> dict:
    return user.delete(userID=userID)

@rout.post(path='/login/', response_model=dict)
def account_login(data:LoginData) -> dict:
    return user.login(data=data)

@rout.put(path='/updatePassword/{userID}', response_model=dict)
def upd_pass(userID: int, new_password: UserPass) -> dict:
    return user.update(userID=userID, new_data=new_password)
