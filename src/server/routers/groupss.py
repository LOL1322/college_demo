from fastapi import APIRouter
from src.server.resolvers import groupss
from src.server.database.models import Groupss

rout = APIRouter(prefix='/groupss', tags=["Groupss"])


@rout.get(path='/get/{groupID}', response_model=dict)
def get_groupss(groupID: int) -> dict:
    return groupss.get(groupID=groupID)


@rout.get(path='/get', response_model=dict)
def get_all_groupss() -> dict:
    return groupss.get_all()


@rout.post(path='/new', response_model=dict)
def new_groupss(data: Groupss) -> dict:
    return groupss.new(data=data)


@rout.put(path='/update/{groupID}', response_model=dict)
def update_groupsss(data: Groupss, groupID: int) -> dict:
    return groupss.update(groupID=groupID, new_data=data)


@rout.delete(path='/delete/{groupID}', response_model=dict)
def delete_groupss(groupID: int) -> dict:
    return groupss.delete(groupID=groupID)