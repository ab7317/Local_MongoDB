import pymongo
import pandas as pd

class MongoDBClient:
    def __init__(self, uri, db_name):

        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

    def get_collections(self):
        collection_names = self.db.list_collection_names()
        #print(collection_names)
        return collection_names

Client = MongoDBClient("mongodb://localhost:27017/", "test_csv")
Client.get_collections()
