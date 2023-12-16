from src.server.database.models import WeekDays
from src.server.database.db_manager import db_manager

def get(weekdayID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM WeekDays WHERE ID = ?''', args=(weekdayID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM WeekDays ''', fetchall=True)

def new(data:WeekDays)-> dict:
    return db_manager.execute(qure='''INSERT INTO WeekDays(day) VALUES (?)''', args=(data.day,))

def update(weekdayID: int, new_data: WeekDays) -> dict:
    return db_manager.execute(qure='''UPDATE WeekDays SET (day) = (?) WHERE ID = ?''', args=(new_data.day, weekdayID))

def delete(weekdayID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM WeekDays WHERE ID = ? ''', args=(weekdayID,))