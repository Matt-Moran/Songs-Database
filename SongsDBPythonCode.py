import pymongo
from pymongo import MongoClient

#Your connection goes in the parentheses, including username and password 
#I have removed my own connection for security purposes
client = pymongo.MongoClient("")

#Getting the database instance
db = client['testing']

#Creating a collection
coll = db['employee']

#Inserting document into a collection
#This is a sample document -- anything can be added
data = [
{
    "Title": "Certified",
    "Album": "Shiesty Season: Certified", 
    "Artists": {
        "Main Artist": "Pooh Shiesty",
        "Featuring Artist": ["Gunna"]
    },
    "Genre": ["Rap", "Hip-Hop"],
    "Length": "3:12",
    "ReleaseDate": {"Month": 4, "Day": 29, "Year": 2022}
}
]
       
#res = coll.insert_many(data)
print("Data inserted ......")

#Retrieving all the records using the find() method
print("Records of the collection: ")
for doc1 in coll.find():
    print(doc1)

#Sample query
#Retrieving records by Pooh Shiesty
print("Songs by Pooh Shiesty")
for doc2 in coll.find({"Artists.Main Artist": "Pooh Shiesty"}, {"Artists.Main Artist":1, "_id":0}):
    print(doc2)