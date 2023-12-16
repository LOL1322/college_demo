from fastapi import APIRouter
from src.server.resolvers import typesusers
from src.server.database.models import TypesUsers

rout = APIRouter(prefix='/typesusers', tags=["TypesUsers"])


@rout.get(path='/get/{typeID}', response_model=dict)
def get_typesusers(typeID: int) -> dict:
    return typesusers.get(typeID=typeID)


@rout.get(path='/get', response_model=dict)
def get_all_typesusers() -> dict:
    return typesusers.get_all()


@rout.post(path='/new', response_model=dict)
def new_typesusers(data: TypesUsers) -> dict:
    return typesusers.new(data=data)


@rout.put(path='/update/{typeID}', response_model=dict)
def update_typesusers(data: TypesUsers, typeID: int) -> dict:
    return typesusers.update(typeID=typeID, new_data=data)


@rout.delete(path='/delete/{typeID}', response_model=dict)
def delete_typesusers(typeID: int) -> dict:
    return typesusers.delete(typeID=typeID)