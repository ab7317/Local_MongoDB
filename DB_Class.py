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
    
    def insert_row_collection(self, collection_name, row_dict):
        self.db[collection_name].insert_one(row_dict)
        print("Row added to collection!")

    def insert_csv_collection(self, collection_name, csv_path):
        csv_dict = pd.read_csv(csv_path).to_dict(orient="records")
        for csv in csv_dict:
           self.db[collection_name].insert_one(csv) 
        print("CSV added!")

    def query_collection_cols(self, collection_name, cols_to_query):
        print(list(self.db[collection_name].find(
        {field: {"$exists": True} for field in cols_to_query},
        {field: 1 for field in cols_to_query + ["_id"]}
        )))