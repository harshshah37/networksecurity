from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://harshshah37:General#99@cluster0.8gmhg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)