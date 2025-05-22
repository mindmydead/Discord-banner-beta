import disnake

class Utils:
    def __init__(self, systemConfig) -> None:
        self.systemConfig = systemConfig
        
    def getGuild(self):
        return self.systemConfig[0]['guildId']
    
    def getInfo(self, member: disnake.Member):
        return {
            "name": member.display_name if member.display_name else 'Пусто',
            "avatar": member.display_avatar.url if member.display_avatar.url else member.default_avatar.url
        }