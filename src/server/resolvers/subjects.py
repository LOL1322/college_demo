from src.server.database.models import Subjects
from src.server.database import db_manager

def get(subjectID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM Subjects WHERE ID = ?''', args=(subjectID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM Subjects ''', fetchall=True)

def new(data:Subjects)-> dict:
    return db_manager.execute(qure='''INSERT INTO Subjects(name) VALUES (?)''', args=(data.name))

def update(subjectID: int, new_data: Subjects) -> dict:
    return db_manager.execute(qure='''UPDATE Subjects SET (name) = (?) WHERE ID = ?''', args=(new_data.name, subjectID))

def delete(subjectID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM Subjects WHERE ID = ? ''', args=(subjectID,))