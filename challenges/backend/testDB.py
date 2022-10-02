from pymongo import MongoClient, InsertOne

uri = "mongodb+srv://pokecluster.bdxw0xo.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./Key/Ashkey.pem')
db = client["Pokedex"]
collection = db["Pokemon"]
print("Connection Successful")

# test collection
x = collection.find_one()
print(x)

client.close()