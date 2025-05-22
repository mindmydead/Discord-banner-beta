from pymongo import MongoClient

from Struct.client.logger import Logger

class DataBase:
    def __init__(self, urlMongo = None, debug = None) -> None:
        self.urlMongo = urlMongo
        self.debug = debug
        
        self.logger = Logger()
        
    def getClient(self):
        client = MongoClient(self.urlMongo)
        return client
    
    def closeClient(self, client: MongoClient):
        client.close()
    
    def Initilization(self):
        if self.urlMongo == None:
            self.logger.error(
                "Error during Data Source initialization"
            )
            return
        
        if self.debug == None:
            self.debug = False
            
        if self.checkConnetctClient():
            self.logger.info(
                "Data Source has been initialized"
            )
        else:
            self.logger.error(
                "Error during Data Source initialization"
            )
    
    def checkConnetctClient(self):
        try:
            client = MongoClient(self.urlMongo)
            client.close()
            return client
        except Exception as er:self.logger.error(
            er
        )
    