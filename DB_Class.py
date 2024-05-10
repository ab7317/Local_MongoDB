import pymongo, os
import pandas as pd

class MongoDBClient:
    def __init__(self, uri, db_name):

        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.db_name = db_name

    def get_databases(self):
        return self.client.list_database_names()

    def get_collections(self):
        return self.db.list_collection_names()
    
    def get_collection_content(self, collection_name:str):
        return list(self.db[collection_name].find())
    
    def insert_row_collection(self, collection_name: str, row_dict: dict):
        self.db[collection_name].insert_one(row_dict)
        print("Row added to collection!")

    def build_csv_path_list(self, csv_dir_path: str):
        ###
        #This function will build a list only of csv files it will ignore any
        #other file types inside the directories
        #It will also only work on a single child directory 
        ###

        full_path_list = []
        dir_list = os.listdir(csv_dir_path)
        for directory in dir_list:
            file_list = os.listdir(f"{csv_dir_path}/{directory}")
            for _file in file_list: 
                if _file == f"{self.db_name}.csv":
                    full_path_list.append(f"{csv_dir_path}/{directory}/{_file}")
        return full_path_list
    
    def breakdown_csv(self):pass



    def insert_csv_collection(self, collection_name: str, csv_path: str):
        try:
            csv_dict = pd.read_csv(csv_path).to_dict(orient="records")
            for csv in csv_dict:
                self.db[collection_name].insert_one(csv) 
                print("CSV added!")
        except:
            print(f"{collection_name}")

    def query_collection_cols(self, collection_name: str, cols_to_query: list):
        ###
        #
        ###

        query = list(self.db[collection_name].find(
        {field: {"$exists": True} for field in cols_to_query},
        {field: 1 for field in cols_to_query + ["_id"]}
        ))

        return pd.DataFrame(query)
    
    def insert_csv_dir_collection(self, csv_full_path_list: list):
        for csv_path in csv_full_path_list:
            collection_name = f"{csv_path.split('/')[-2]}_{csv_path.split('/')[-1]}"
            self.insert_csv_collection(collection_name, csv_path)
        print("Files added")
