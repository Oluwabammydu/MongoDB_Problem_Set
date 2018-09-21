import json
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client.Developer_CV_DB
collection = db.clientForm
Developer_client = [
    {"_id": 1, "name": "Chizokam", "skills": "python" ,
        "github repo link": "https://github.com/Chiazokam"} ,
    {"_id": 2, "name": "Emmanuel", "skills": "jquery" ,
        "github repo link": "https://github.com/Emman77240"} ,
    {"_id": 3, "name": "Marshall", "skills": "extreme programming" ,
        "github repo link": "https://github.com/uimarshall"} ,
    {"_id": 4, "name": "Emeka", "skills": "agile programming" ,
        "github repo link": "https://github.com/Shyzay"}
]
#collection.insert_many(Developer_client)
print('***************************************', '\n')
# Printing the number of documents in the collections

print("The number of documents in my collection: ", collection.count_documents({}))
print('***************************************', '\n')
# query entries in the collection using regex
myquery = {"name": {"$regex": "^Em"}}

mydoc = collection.find(myquery)
print("All entries with 'Em' in field 'skills': ", collection.count_documents(myquery))
# Print all entries
print('***************************************', '\n')
print('Printing all entries:')
# iterate through the collection and read the entries
for x in collection.find():
    print(json.dumps(x, indent=2))
