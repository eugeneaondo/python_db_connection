from pymongo import MongoClient


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://eugeneaondo11:mongo123@cluster0.wpfxevu.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

for db_name in client.list_database_names():
    print(db_name)

