from src.server.database.models import TypesUsers
from src.server.database import db_manager

def get(typeID: int) -> dict:
    return db_manager.execute(qure='''SELECT * FROM TypesUsers WHERE ID = ?''', args=(typeID,))

def get_all() -> dict:
    return db_manager.execute(qure='''SELECT * FROM TypesUsers ''', fetchall=True)

def new(data: TypesUsers)-> dict:
    return db_manager.execute(qure='''INSERT INTO TypesUsers(title, power_level) VALUES (?, ?)''', args=(data.title, data.power_level))

def update(typeID: int, new_data: TypesUsers) -> dict:
    return db_manager.execute(qure='''UPDATE TypesUsers SET (title, power_level) = (?, ?) WHERE ID = ?''', args=(new_data.title, new_data.power_level, typeID))

def delete(typeID: int) -> dict:
    return db_manager.execute(qure=''' DELETE FROM TypesUsers WHERE ID = ? ''', args=(typeID,))
                            
