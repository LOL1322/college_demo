from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    ID: Optional[int]


class TypesUsers(ModifyBaseModel):
    title: str
    power_level: int


class Subjects(ModifyBaseModel):
    name: str


class WeekDays(ModifyBaseModel):
    day: str


class Groupss(ModifyBaseModel):
    title: str
    tutor: str 


class Shedules(ModifyBaseModel):
    day_id: int
    note: str


class User(ModifyBaseModel):
    type_id: int
    login: str
    password: str
    group_id: int


class Schedules_of_groupss_of_subjects(ModifyBaseModel):
    shedule_id: int 
    subject_id: int
    group_id: int
    user_id: int


class UserPass(BaseModel):
    password: str


class LoginData(BaseModel):
    login: str 
    password: str