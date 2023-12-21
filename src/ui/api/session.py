from ui.api import resolvers
from src.server.database.models import User, UserPass, LoginData

class Session:
    auth: bool = False
    user: User = User(
            ID=-1,
            type_id=1,
            login='',
            password=''
        )
    error: str = None
    server_available: bool = False



    def login(self, login: str, password: str):
        answer: dict = resolvers.login(user=LoginData(login=login, password=password))
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
            
            case 200:
                self.error = None
                self.user = User(ID=answer["result"]["ID"],
                                 type_id=answer['result']['type_id'],
                                 login=answer["result"]["login"],
                                 password=answer["result"]["password"])
                
                self.auth = True



    def register(self, type_id: int, login: str, password: str):
        answer: dict = resolvers.register(user=User(type_id=type_id, login=login, password=password))
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
                
            case 200:
                self.error = None
                self.user = User(ID=answer["result"]["ID"],
                                 type_id=answer['result']['type_id'],
                                 login=answer["result"]["login"],
                                 password=answer["result"]["password"])
                


    def update(self, password: str):
        answer: dict = resolvers.update(UserPass(password=str(password)), userID=self.user.ID)
        match answer["code"]:
            case 400:
                self.error = answer["msg"]

            case 200:
                self.error = None

    def delete(self) -> None:
        resolvers.delete(self.user.ID)
        self.leave()

    def leave(self) -> None:
        self.user.ID = -1
        self.user.type_id = -1
        self.user.login = ''
        self.user.password = ''
        self.auth = False
          