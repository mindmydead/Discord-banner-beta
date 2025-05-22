import os

from Struct.client import Client

os.system("cls" if os.name == "nt" else "clear")
botClient = Client()
botClient.CreateClient()
botClient.initClient()
