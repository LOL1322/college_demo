from fastapi import APIRouter
from src.server.resolvers import shedules
from src.server.database.models import Shedules

rout = APIRouter(prefix='/shedules', tags=["Shedules"])


@rout.get(path='/get/{sheduleID}', response_model=dict)
def get_shedules(sheduleID: int) -> dict:
    return shedules.get(sheduleID=sheduleID)


@rout.get(path='/get', response_model=dict)
def get_all_shedules() -> dict:
    return shedules.get_all()


@rout.post(path='/new', response_model=dict)
def new_shedules(data: Shedules) -> dict:
    return shedules.new(data=data)


@rout.put(path='/update/{sheduleID}', response_model=dict)
def update_shedules(data: Shedules, sheduleID: int) -> dict:
    return shedules.update(sheduleID=sheduleID, new_data=data)


@rout.delete(path='/delete/{sheduleID}', response_model=dict)
def delete_shedules(sheduleID: int) -> dict:
    return shedules.delete(sheduleID=sheduleID)