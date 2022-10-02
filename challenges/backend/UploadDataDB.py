import pymongo
import json
from pymongo import MongoClient, InsertOne

uri = "mongodb+srv://pokecluster.bdxw0xo.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./Key/Ashkey.pem')
db = client.Pokedex
collection = db.Pokemon
requesting = []

with open(r"pokemons.json") as f:
    data = json.loads(f.read())
    for jsonObj in data:
        requesting.append(InsertOne(jsonObj))

result = collection.bulk_write(requesting)
client.close()