import os
from Struct.client.logger import Logger

class BaseEvent:
    def __init__(self, bot, command: bool = None,
                 event: bool = None, task: bool = None) -> None:
        self.command = command
        self.event = event
        self.task = task
        self.bot = bot
        self.logger = Logger()
    
    def Initialization(self):
        if self.command == True:
            self.loadCommands()
        
        if self.event == True:
            self.loadEvents()
        
        if self.task == True:
            self.loadTasks()
    
    def loadCommands(self):
        try:
            for filename in os.listdir("src/App/Commands"):
                if filename.endswith(".py"):
                    self.logger.info(
                        f"Command {filename[:-3]} initialization"
                    )
                    self.bot.load_extension(f"App.Commands.{filename[:-3]}")
        except Exception as er: self.logger.error(
            er
        )
    
    def loadEvents(self):
        try:
            for filename in os.listdir("src/App/Listeners"):
                if filename.endswith(".py"):
                    self.logger.info(
                        f"Listener {filename[:-3]} initialization"
                    )
                    self.bot.load_extension(f"App.Listeners.{filename[:-3]}")
        except Exception as er: self.logger.error(
            er
        )
        
    def loadTasks(self):
        try:
            for filename in os.listdir("src/App/Tasks"):
                if filename.endswith(".py"):
                    self.logger.info(
                        f"Task {filename[:-3]} initialization"
                    )
                    self.bot.load_extension(f"App.Tasks.{filename[:-3]}")
        except Exception as er: self.logger.error(
            er
        )