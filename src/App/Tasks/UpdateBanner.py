from disnake.ext import commands, tasks
import disnake

from Struct.client import Client
from Struct.data.user.userSelectVoice import UserSelectVoice
from Struct.utils.Pillow.Banner import DrawBanner

class UpdateBannerTask(commands.Cog):
    def __init__(self, bot: disnake.BotIntegration):
        self.bot = bot
        
        self.logger = Client().logger
        self.Utls = Client().BotUtils
        
        self.systemConfig = Client().systemConfig
        
        self.UserDataBaseSelect = UserSelectVoice()
        self.DrawUpdate = DrawBanner()
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.updateBannerStat.start()

    @tasks.loop(seconds=30)
    async def updateBannerStat(self):
        userTopVoice = await self.UserDataBaseSelect.SelectTimeUserTop()
        guild = self.bot.get_guild(self.systemConfig[0]['guildId'])
        self.DrawUpdate.guild = guild
        await self.DrawUpdate.DrawUpdateBanner(userTopVoice)

def setup(bot):
    bot.add_cog(UpdateBannerTask(bot))