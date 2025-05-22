from disnake.ext import commands
import disnake

import time

from Struct.client import Client
from Struct.data.user.userUpdateVoice import UserUpdateVoice

connected_users = dict()
class VoiceUserListener(commands.Cog):
    def __init__(self, bot: disnake.BotIntegration) -> None:
        self.bot = bot
        
        self.logger = Client().logger
        self.Utils = Client().BotUtils
        
        self.UserDataBaseUpdate = UserUpdateVoice()
        
    async def TimeUpdate(self, user: disnake.Member, voiceTime):
        await self.UserDataBaseUpdate.UpdateTime(
            user=user,
            voiceTime=voiceTime
        )
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
        in_voice_channel = member.voice
        if in_voice_channel and member not in connected_users.keys():
            connected_users[member] = time.time()
        elif not in_voice_channel and member in connected_users.keys():
            time_voice = round(time.time() - connected_users[member])
            
            del connected_users[member]   
            
            await self.TimeUpdate(user=member, voiceTime=round(time_voice))
            
def setup(bot):
    bot.add_cog(VoiceUserListener(bot))
