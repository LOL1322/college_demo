from pydantic import BaseModel


class ModifyBaseModel(BaseModel):
    ID: int


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


class Users(ModifyBaseModel):
    type_id: int
    login: str
    password: str
    group_id: int


class Schedules_of_groupss_of_subjects(ModifyBaseModel):
    shedule_id: int 
    subject_id: int
    group_id: int
    user_id: int


    