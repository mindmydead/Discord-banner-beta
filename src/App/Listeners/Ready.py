import disnake
from disnake.ext import commands

from Struct.client import Client

class ReadyListerner(commands.Cog):
    def __init__(self, bot: disnake.BotIntegration) -> None:
        self.bot = bot
        
        self.logger = Client().logger
        self.Utils = Client().BotUtils
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(
        f"""{self.bot.user.name} Подключился к серверам Discord"""
        )
        self.logger.info(
        f"""Серверов где находится бот: {len(self.bot.guilds)}"""
        )
        
def setup(bot):
    bot.add_cog(ReadyListerner(bot))