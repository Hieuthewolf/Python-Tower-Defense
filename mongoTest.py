import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://hieuthewolf:hieutrung123@cluster0-qcx63.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["Python_Tower_Defense"]
collection = db["high_scores"]

post = {"_id": 4, "name": "Hieu"}
post2 = {"_id": 5, "name": "Hieuew"}

# res = collection.update_one({"_id" : 0}, {"$inc": {"score" : 1}})

post_count = collection.count_documents({"name": "Hieu"})
print(post_count)


# collection.count_documents()
# collection.delete_many()
# collection.delete_one()
# collection.update_one({})
# collection.update_many({})

# collection.insert_one()
# collection.insert_many()

# collection.find_and_modify()
# collection.find_one_and_replace()
# collection.find_one_and_update()
# collection.find_one()

# colleciton.find()