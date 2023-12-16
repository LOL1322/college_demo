from fastapi import APIRouter
from src.server.resolvers import subjects
from src.server.database.models import Subjects

rout = APIRouter(prefix='/subjects', tags=["Subjects"])


@rout.get(path='/get/{subjectID}', response_model=dict)
def get_subjects(subjectID: int) -> dict:
    return subjects.get(subjectID=subjectID)


@rout.get(path='/get', response_model=dict)
def get_all_subjects() -> dict:
    return subjects.get_all()


@rout.post(path='/new', response_model=dict)
def new_subjects(data: Subjects) -> dict:
    return subjects.new(data=data)


@rout.put(path='/update/{subjectID}', response_model=dict)
def update_subjects(data: Subjects, subjectID: int) -> dict:
    return subjects.update(subjectID=subjectID, new_data=data)


@rout.delete(path='/delete/{subjectID}', response_model=dict)
def delete_subjects(subjectID: int) -> dict:
    return subjects.delete(subjectID=subjectID)
    