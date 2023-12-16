from fastapi import APIRouter
from src.server.resolvers import weekdays
from src.server.database.models import WeekDays

rout = APIRouter(prefix='/weekdays', tags=["WeekDays"])


@rout.get(path='/get/{weekdayID}', response_model=dict)
def get_weekdays(weekdayID: int) -> dict:
    return weekdays.get(weekdayID=weekdayID)


@rout.get(path='/get', response_model=dict)
def get_all_weekdays() -> dict:
    return weekdays.get_all()


@rout.post(path='/new', response_model=dict)
def new_weekdays(data: WeekDays) -> dict:
    return weekdays.new(data=data)


@rout.put(path='/update/{weekdayID}', response_model=dict)
def update_weekdays(data: WeekDays, weekdayID: int) -> dict:
    return weekdays.update(weekdayID=weekdayID, new_data=data)


@rout.delete(path='/delete/{weekdayID}', response_model=dict)
def delete_weekdays(weekdayID: int) -> dict:
    return weekdays.delete(weekdayID=weekdayID)