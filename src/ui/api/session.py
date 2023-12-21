from src.ui.api import resolvers
from src.server.database.models import User, UserPass, LoginData

class Session:
    auth: bool = False
    user: User = User(
            ID=-1,
            type_id=-1,
            group_id=-1,
            login='',
            password=''
        )
    error: str = None
    server_available: bool = False

    def check_connection(self) -> bool:
        self.server_available = type(resolvers.check_available()) is bool

    def login(self, login: str, password: str):
        answer: dict = resolvers.login(user=LoginData(login=login, password=password))
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
            
            case 200:
                self.error = None
                self.user = User(ID=answer["result"]["ID"],
                                 type_id=answer['result']['type_id'],
                                 group_id=answer['result']['group_id'],
                                 login=answer["result"]["login"],
                                 password=answer["result"]["password"])
                
                self.auth = True



    def register(self, group_id: int, type_id: int, login: str, password: str):
        answer: dict = resolvers.register(user=User(ID=0, type_id=int(type_id), login=login, password=password, group_id=int(group_id)))
        match answer["code"]:
            case 400:
                self.error = answer["msg"]
                
            case 200:
                self.error = None
                self.user = User(ID=answer["result"]["ID"],
                                 type_id=answer['result']['type_id'],
                                 group_id=answer['result']['group_id'],
                                 login=answer["result"]["login"],
                                 password=answer["result"]["password"])
                


    def update(self, password: str):
        answer: dict = resolvers.update(UserPass(password=str(password)), ID=self.user.ID)
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
        self.group_id = -1
        self.user.login = ''
        self.user.password = ''
        self.auth = False
          