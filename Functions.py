import pandas as pd
import sys

db_class_path = "C:/Users/Administrator/Code/MongoDB"

sys.path.append(db_class_path)
import mongo_class as mc

Client = mc.MongoDBClient("mongodb://localhost:27017/", "test_new")

#print(Client.get_collections())

#print(Client.get_collection_content("CoinM"), "\n##########################")

result = Client.query([{"Date": "2024-05-10"}, {"Time": "12-00"}], "Breakdown")

print(result)

sum_of_atom = result['Total'].sum()

print(sum_of_atom)

csv_files = Client.build_csv_path_list("C:/Users/Administrator/Code/rusty_snapshots/snapshots")

for csv in csv_files:
    Client.insert_csv_collection(csv.split("/")[-1][:-4], csv)
