import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb+srv://Ash:Ketchum@pokecluster.bdxw0xo.mongodb.net/?retryWrites=true&w=majority")
db = client.Pokedex
collection = db.Pokemon
requesting = []

with open(r"pokemons.json") as f:
    data = json.loads(f.read())
    for jsonObj in data:
        requesting.append(InsertOne(jsonObj))


result = collection.bulk_write(requesting)
client.close()

"""

with open("pokemons.json") as f:
    data = json.loads(f.read())
    for jsonObj in data:
        requesting.append(InsertOne(jsonObj))

result = collection.bulk_write(requesting)
client.close()

"""