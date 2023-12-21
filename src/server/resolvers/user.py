from src.server.database.models import User, UserPass
from src.server.database.db_manager import db_manager

def get(userID: int) -> dict:
    res = db_manager.execute(qure='''SELECT * FROM User WHERE ID = ?''', args=(userID,))

    res["result"] = None if not res["result"] else User(
        ID=res["result"][0],
        type_id=res["result"][1],
        login=res["result"][2],
        password=res["result"][3],
        group_id=res["result"][4]
    )

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res



def get_all() -> dict:
    res = db_manager.execute(qure='''SELECT * FROM User ''', fetchall=True)

    list_accounts = []

    if res["result"]:
        for account in res["result"]:
            list_accounts.append(User(
                ID=account[0],
                type_id=account[1],
                login=account[2],
                password=account[3],
                group_id=account[4]

           ))
            
    res["result"] = None if len(list_accounts) == 0 else list_accounts

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

def new(data: User)-> dict:
    res = db_manager.execute(qure='''INSERT INTO User(type_id, login, password, group_id) VALUES (?, ?, ?, ?) RETURNING ID''', args=(data.type_id, data.login, data.password, data.group_id))    
    
    res["result"] = None if not res["result"] else get(res["result"][0])["result"] 

    return res

def update(userID: int, new_data: User) -> dict:
    res = db_manager.execute(qure='''UPDATE User SET (password) = (?) WHERE ID = ?''', args=(new_data.password, userID))

    res["result"] = get(userID = userID )["result"]

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def delete(userID: int) -> dict:
    check_user = get(userID=userID)["result"]
    res = db_manager.execute(qure=''' DELETE FROM User WHERE ID = ? ''', args=(userID,))

    if check_user is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

def login(data:User):
    res = db_manager.execute(qure=''' SELECT ID FROM User WHERE login = ? AND password = ? ''', args=(data.login, data.password))

    if res["result"] is None:
        res["msg"] = "Incorrect login or password"
        res["code"] = 400
        res["error"] = True
        return res

    return get(userID=res["result"][0])       