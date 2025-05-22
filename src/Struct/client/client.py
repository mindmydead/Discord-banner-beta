import disnake
from disnake.ext import commands

from config import system, database, banner

from Struct.data.database import DataBase
from Struct.base.BaseEvent import BaseEvent
from Struct.client.logger import Logger
from Struct.client.utils import Utils

class Client:
    def __init__(self, bot=None) -> None:
        self.bot = bot
        
        self.logger = Logger()
        self.database = DataBase()
        self.BaseEvent = BaseEvent(self.bot)
        
        self.systemConfig = system
        self.bannerConfig = banner
        
        self.BotUtils = Utils(self.systemConfig)

    def CreateClient(self):
        command_sync_flags_settings = commands.CommandSyncFlags.default()
        command_sync_flags_settings.sync_commands_debug = False
        bot = commands.Bot(
            command_prefix="dev.set:",
            command_sync_flags=command_sync_flags_settings,
            intents=disnake.Intents.all()
        )
        bot.remove_command('help')
        
        self.bot = bot
        
    def initClient(self):
        self.database.urlMongo = database['client']
        self.database.debug = False
        self.database.Initilization()
        
        self.BaseEvent.event = True
        self.BaseEvent.task = True
        self.BaseEvent.bot = self.bot
        self.BaseEvent.Initialization()
        
        try:
            self.logger.info("Bot started")
            self.bot.run(system[0]['token'])
        except Exception as er: self.logger.error(er)
