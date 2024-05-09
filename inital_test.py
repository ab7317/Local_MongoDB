import pymongo
import pandas as pd

csv = pd.read_csv("")

mongo_uri = "mongodb://localhost:27017/"

client = pymongo.MongoClient(mongo_uri)
db = client["test"]

collection_name = "test_collection_2"
collection = db[collection_name]

result = collection.insert_one({"key": "value_2"})  # Example document (key-value pair)

# Check if the collection was created successfully
if result.acknowledged:
    print(f"Collection '{collection_name}' created successfully!")
else:
    print(f"Failed to create collection '{collection_name}'")

print(db.list_collection_names())

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client["test"]

    # Access the specified collection
    collection = db[collection_name]

    # Retrieve all documents (values) in the collection
    documents = collection.find()

    # Print the values of each document
    print(f"Values in '{collection_name}':")
    for doc in documents:
        print(doc)

except pymongo.errors.ConnectionFailure:
    print("Failed to connect to MongoDB.")
