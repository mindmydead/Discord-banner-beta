from disnake.ext import commands, tasks
import disnake

from Struct.client import Client
from Struct.data.user.userUpdateVoice import UserUpdateVoice

class ResetTimeTask(commands.Cog):
    def __init__(self, bot: disnake.BotIntegration):
        self.bot = bot
        
        self.logger = Client().logger
        self.Utls = Client().BotUtils
        
        self.UserDataBaseUpdate = UserUpdateVoice()
        self.last = 0
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.resetTable.start()
        self.last = 0

    @tasks.loop(seconds=7200)
    async def resetTable(self):
        if self.last == 0:
            self.last += 1
        else:
            await self.UserDataBaseUpdate.ResetAllTable()

def setup(bot):
    bot.add_cog(ResetTimeTask(bot))