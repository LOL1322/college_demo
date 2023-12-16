from fastapi import APIRouter
from src.server.resolvers import schedules_of_groupss_of_subjects
from src.server.database.models import Schedules_of_groupss_of_subjects

rout = APIRouter(prefix='/schedules_of_groupss_of_subjects', tags=["Schedules_of_groupss_of_subjects"])


@rout.get(path='/get/{ID}', response_model=dict)
def get_schedules_of_groupss_of_subjects(ID: int) -> dict:
    return schedules_of_groupss_of_subjects.get(ID=ID)


@rout.get(path='/get', response_model=dict)
def get_all_schedules_of_groupss_of_subjects() -> dict:
    return schedules_of_groupss_of_subjects.get_all()


@rout.post(path='/new', response_model=dict)
def new_schedules_of_groupss_of_subjects(data: Schedules_of_groupss_of_subjects) -> dict:
    return schedules_of_groupss_of_subjects.new(data=data)


@rout.put(path='/update/{ID}', response_model=dict)
def update_schedules_of_groupss_of_subjects(data: Schedules_of_groupss_of_subjects, ID: int) -> dict:
    return schedules_of_groupss_of_subjects.update(ID=ID, new_data=data)


@rout.delete(path='/delete/{ID}', response_model=dict)
def delete_schedules_of_groupss_of_subjects(ID: int) -> dict:
    return schedules_of_groupss_of_subjects.delete(ID=ID)