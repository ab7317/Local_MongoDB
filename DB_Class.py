import pymongo, os
import pandas as pd

class MongoDBClient:
    def __init__(self, uri, db_name):

        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

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
                if _file[-3:] == "csv":
                    full_path_list.append(f"{csv_dir_path}/{directory}/{_file}")
        return full_path_list

    def insert_csv_collection(self, collection_name: str, csv_path: str):
        try:
            df = pd.read_csv(csv_path)
            df['Time'] = csv_path.split('/')[-2].split("_")[1]
            df['Date'] = csv_path.split('/')[-2].split("_")[0]
            csv_dict = df.to_dict(orient="records")
            for csv in csv_dict:
                #self.db[collection_name].create_index([('Symbol', 1)], unique=True)
                self.db[collection_name].insert_one(csv) 
        except Exception as e:
            print(f"{collection_name} ERROR: {e}")

    def query(self, query_filter: list, collection_name: str):

        try:
            combined_filter = {'$and': query_filter}
            result = self.db[collection_name].find(combined_filter)
            
            return pd.DataFrame(list(result))
        except Exception as e:
            print(f'Error: {e}')  
