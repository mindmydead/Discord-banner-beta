import disnake

from Struct.data.database import DataBase

class UserSelectVoice:
    def __init__(self) -> None:
        self.client = DataBase()
        
    async def SelectTimeUser(self, user: disnake.Member):
        client = self.client.getClient()
        db = client['BannerBot']
        collection = db['VoiceUser']
        
        userDb = collection.find_one({
            "_id": f"{user.id}" 
        })
        
        self.client.closeClient(client)
        return userDb['voice']
    
    async def SelectTimeUserTop(self):
        client = self.client.getClient()
        db = client['BannerBot']
        collection = db['VoiceUser']
        
        userDb = collection.find_one({}, sort=[("voice", -1)])
        
        self.client.closeClient(client)
        return userDb['_id']
