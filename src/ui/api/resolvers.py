import requests
from src.server.database.models import TypesUsers, User, UserPass, LoginData
import settings


def server_available(func):
    def need_it(*arg, **kwargs):
        try:
            requests.get(url=settings.URL)
            return func(*arg, **kwargs)
        except requests.exceptions.ConnectionError as ex:
            return {"code":400, "msg": str(ex), "error": True, "result": None}
        
    return need_it

@server_available
def check_available():
    return True

@server_available
def register(user:User) -> dict:
    data = f'{{"ID": {user.ID}, "login": "{user.login}", "password": "{user.password}", "group_id": {user.group_id}, "type_id": {user.type_id}}}'
    return requests.post(url=f'{settings.URL}/user/new', data=data).json()


@server_available
def login(user:LoginData) -> dict:
    data = f'{{"login": "{user.login}", "password": "{user.password}"}}'
    return requests.post(url=f'{settings.URL}/user/login/', data=data).json()


@server_available
def update(password: UserPass, ID: int) -> dict:
    data = f'{{"password": "{password.password}"}}'
    return requests.put(url=f'{settings.URL}/user/updatePassword/{ID}', data=data).json()


@server_available
def delete(ID: int) -> dict:
    return requests.delete(url=f'{settings.URL}/user/delete/{ID}').json()





    