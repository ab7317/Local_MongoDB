import pymongo
import pandas as pd

class MongoDBClient:
    def __init__(self, uri, db_name):

        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

    def get_collections(self):
        return self.db.list_collection_names()
    
    def get_collection_content(self, collection_name):
        return list(self.db[collection_name].find())
    
    def insert_row_collection(self, )


Client = MongoDBClient("mongodb://localhost:27017/", "test_csv")
print(Client.get_collection_content("2024-05-09_17-00_CoinM"))
