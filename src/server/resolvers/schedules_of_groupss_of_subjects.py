from src.server.database.models import Schedules_of_groupss_of_subjects
from src.server.database.db_manager import db_manager

def get(ID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM Schedules_of_groupss_of_subjects WHERE ID = ?''', args=(ID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM Schedules_of_groupss_of_subjects ''', fetchall=True)

def new(data: Schedules_of_groupss_of_subjects)-> dict:
    return db_manager.execute(qure='''INSERT INTO Schedules_of_groupss_of_subjects(shedule_id, subject_id, group_id, user_id) VALUES (?, ?, ?, ?)''', args=(data.shedule_id, data.subject_id, data.group_id, data.user_id))

def update(ID: int, new_data: Schedules_of_groupss_of_subjects) -> dict:
    return db_manager.execute(qure='''UPDATE Schedules_of_groupss_of_subjects SET (shedule_id, subject_id, group_id, user_id) = (?, ?, ?, ?) WHERE ID = ?''', args=(new_data.shedule_id, new_data.subject_id, new_data.group_id, new_data.user_id, ID))

def delete(ID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM Schedules_of_groupss_of_subjects WHERE ID = ? ''', args=(ID,))