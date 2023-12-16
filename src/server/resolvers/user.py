from src.server.database.models import User
from src.server.database.db_manager import db_manager

def get(userID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM User WHERE ID = ?''', args=(userID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM User ''', fetchall=True)

from src.server.database.models import User
def new(data: User)-> dict:
    return db_manager.execute(qure='''INSERT INTO User(type_id, login, password, group_id) VALUES (?, ?, ?, ?)''', args=(data.type_id, data.login, data.password, data.group_id))

def update(userID: int, new_data: User) -> dict:
    return db_manager.execute(qure='''UPDATE User SET (type_id, login, password, group_id) = (?, ?, ?, ?) WHERE ID = ?''', args=(new_data.type_id, new_data.login, new_data.password, new_data.group_id, userID))

def delete(userID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM User WHERE ID = ? ''', args=(userID,))