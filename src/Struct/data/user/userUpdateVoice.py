import disnake

from Struct.data.database import DataBase

class UserUpdateVoice:
    def __init__(self) -> None:
        self.client = DataBase()
        
    async def InsertNewUser(self, user: disnake.Member, voiceTime):
        client = self.client.getClient()
        db = client['BannerBot']
        collection = db['VoiceUser']
        
        userDb = collection.find_one({
            "_id": f"{user.id}" 
        })
        if userDb == None:
            collection.insert_one(
                {"_id": f"{user.id}", 
                "voice": {voiceTime}
                }
            )

        self.client.closeClient(client)
        
    async def ResetAllTable(self):
        client = self.client.getClient()
        db = client['BannerBot']
        collection = db['VoiceUser']
        
        collection.delete_many({})

        self.client.closeClient(client)
        
    async def UpdateTime(self, user: disnake.Member, voiceTime):
        client = self.client.getClient()
        db = client['BannerBot']
        collection = db['VoiceUser']
        
        userDb = collection.find_one({
            "_id": f"{user.id}" 
        })
        if userDb == None:
            collection.insert_one(
                {"_id": f"{user.id}", 
                "voice": voiceTime
                }
            )
        else:
            collection.update_one({"_id": f"{user.id}"}, {"$inc": {"voice": voiceTime}})

        self.client.closeClient(client)