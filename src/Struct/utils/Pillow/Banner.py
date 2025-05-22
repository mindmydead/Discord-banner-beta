from Struct.client import Client

import io
import requests
import disnake
from PIL import Image, ImageDraw, ImageFont

class DrawBanner:
    def __init__(self, guild = None) -> None:
        self.guild = guild
        self.user = None
        self.userName = None
        self.bannerConfig = Client().bannerConfig
    
    async def initUser(self, userId):
        user = self.guild.get_member(int(userId))
        self.user = user.id
        self.userName = user.name
    
    async def AddAvatarUser(self, background):
        X = self.bannerConfig['userAvatarX']
        Y = self.bannerConfig['userAvatarY']
        
        sizeW = self.bannerConfig['sizeWavatar']
        sizeH = self.bannerConfig['sizeHavatar']
        
        user = self.guild.get_member(int(self.user))
        
        avatar_url = user.avatar.url
        avatar_image = Image.open(requests.get(avatar_url, stream=True).raw).convert("RGBA")

        mask = Image.new("L", avatar_image.size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, mask.width, mask.height), fill=255)
        avatar_image.putalpha(mask)

        avatar_image = avatar_image.resize((sizeW, sizeH))
        
        background.paste(avatar_image, (X, Y), avatar_image)
    
    async def AddUserStatus(self, draw, font):
        X = self.bannerConfig['userUserStatusX']
        Y = self.bannerConfig['userUserStatusY']
        
        userStatusWidth = self.bannerConfig['userStatusWidth']
        
        user = self.guild.get_member(int(self.user))
        
        activ = False
        for activity in user.activities:
            if isinstance(activity, disnake.CustomActivity):
                activ = True
                status_text = activity.state or "Не указан"
                if len(status_text) >= userStatusWidth:
                    status_text = status_text[:userStatusWidth-1] + '...'
                draw.text((X, Y), str(status_text), fill="#B0B0B0", font=font)
                
        if activ == False:
            draw.text((X, Y), "Отсутсвует", fill="#B0B0B0", font=font)
    
    async def AddUserName(self, draw, font):
        X = self.bannerConfig['userUserNameX']
        Y = self.bannerConfig['userUserNameY']
        
        userNameWidth = self.bannerConfig['userNameWidth']
        user_name = self.userName
        if len(user_name) >= userNameWidth:
            user_name = user_name[:userNameWidth-1] + '...'
        
        draw.text((X, Y), str(user_name), font=font)
    
    async def AddUserVoice(self, draw, font):
        X = self.bannerConfig['userUserVoiceX']
        Y = self.bannerConfig['userUserVoiceY']
        
        voice = len([m for m in self.guild.members if m.voice])
        
        text_bbox1 = draw.textbbox((0, 0), f"{voice}", font=font)
        text_width1 = text_bbox1[2] - text_bbox1[0]
        draw.text(((X - text_width1 / 2), Y), str(voice), font=font)
    
    async def AddTotalUsers(self, draw, font):
        X = self.bannerConfig['userTotalUsersX']
        Y = self.bannerConfig['userTotalUsersY']
        
        total = len(self.guild.members)
        
        text_bbox1 = draw.textbbox((0, 0), f"{total}", font=font)
        text_width1 = text_bbox1[2] - text_bbox1[0]
        draw.text(((X - text_width1 / 2), Y), str(total), font=font)
    
    async def DrawUpdateBanner(self, userId):
        await self.initUser(userId)
        
        pathImage = self.bannerConfig['pathImage']
        pathFontOnline = self.bannerConfig['pathFontOnline']
        pathFontTotal = self.bannerConfig['pathFontTotal']
        pathFontUserName = self.bannerConfig['pathFontUsername']
        pathFontStatus = self.bannerConfig['pathFontStatu']
        
        pathFontOnlineSize = self.bannerConfig['pathFontOnlineSize']
        pathFontTotalSize = self.bannerConfig['pathFontTotalSize']
        pathFontUserNameSize = self.bannerConfig['pathFontUsernameSize']
        pathFontStatusSize = self.bannerConfig['pathFontStatuSize']
        
        background = Image.open(pathImage)
        draw = ImageDraw.Draw(background)
        
        fontOnline = ImageFont.truetype(pathFontOnline, size=pathFontOnlineSize)
        fontTotal = ImageFont.truetype(pathFontTotal, size=pathFontTotalSize)
        fontUserName = ImageFont.truetype(pathFontUserName, size=pathFontUserNameSize)
        fontStatus = ImageFont.truetype(pathFontStatus, size=pathFontStatusSize)

        await self.AddUserVoice(draw, fontOnline)
        await self.AddTotalUsers(draw, fontTotal)
        await self.AddUserName(draw, fontUserName)
        await self.AddUserStatus(draw, fontStatus)
        await self.AddAvatarUser(background)
        
        img_bytes = io.BytesIO()
        background.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        bytes =  img_bytes.read()
        await self.guild.edit(banner=bytes)
        