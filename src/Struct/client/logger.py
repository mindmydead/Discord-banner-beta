from datetime import datetime

class Logger: 
    def __init__(self) -> None:
        pass
    
    def getDate(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M')

    def error(self, msg: str):
        print(
            f"\033[91m[{self.getDate()}] {msg}\033[0m\n"
    )
        
    def info (self, msg:str):
        print(
            f"\033[94m[{self.getDate()}] {msg}\033[0m\n"
    )