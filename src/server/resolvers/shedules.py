from src.server.database.models import Shedules
from src.server.database import db_manager

def get(sheduleID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM Shedules WHERE ID = ?''', args=(sheduleID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM Shedules ''', fetchall=True)

def new(data:Shedules)-> dict:
    return db_manager.execute(qure='''INSERT INTO Shedules(day_id, note) VALUES (?, ?)''', args=(data.day_id, data.note))

def update(sheduleID: int, new_data: Shedules) -> dict:
    return db_manager.execute(qure='''UPDATE Shedules SET (day_id, note) = (?, ?) WHERE ID = ?''', args=(new_data.day_id, sheduleID))

def delete(sheduleID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM Shedules WHERE ID = ? ''', args=(sheduleID,))