from src.server.database.models import Groupss
from src.server.database import db_manager

def get(groupID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM Groupss WHERE ID = ?''', args=(groupID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM Groupss ''', fetchall=True)

def new(data: Groupss)-> dict:
    return db_manager.execute(qure='''INSERT INTO Groupss(title, tutor) VALUES (?, ?)''', args=(data.title, data.tutor))

def update(groupID: int, new_data: Groupss) -> dict:
    return db_manager.execute(qure='''UPDATE Groupss SET (title, tutor) = (?, ?) WHERE ID = ?''', args=(new_data.title, new_data.tutor, groupID))

def delete(groupID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM Groupss WHERE ID = ? ''', args=(groupID,))