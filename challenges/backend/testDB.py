from queue import Empty
import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb+srv://Ash:Ketchum@pokecluster.bdxw0xo.mongodb.net/?retryWrites=true&w=majority")
db = client["PokeDex"]
collection = db["test"]
print("Connection Successful")

x = collection.find_one()
print(x)

client.close()