from src.server.database.models import Users
from src.server.database import db_manager

def get(userID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM Users WHERE ID = ?''', args=(userID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM Users ''', fetchall=True)

def new(data: Users)-> dict:
    return db_manager.execute(qure='''INSERT INTO Users(type_id, login, password, group_id) VALUES (?, ?, ?, ?)''', args=(data.type_id, data.login, data.password, data.group_id))

def update(userID: int, new_data: Users) -> dict:
    return db_manager.execute(qure='''UPDATE TypesUsers SET (type_id, login, password, group_id) = (?, ?, ?, ?) WHERE ID = ?''', args=(new_data.type_id, new_data.login, new_data.password, new_data.group_id, userID))

def delete(userID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM Users WHERE ID = ? ''', args=(userID,))