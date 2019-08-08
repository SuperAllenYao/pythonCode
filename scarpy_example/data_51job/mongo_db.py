from pymongo import MongoClient


class Mongo_Client(object):
    def __init__(self):
        client = MongoClient(host="localhost", port=27017)
        mydb = client["db_51job"]
        self.mycollection = mydb["job_collection"]

    def insert_db(self, item):
        self.mycollection.insert_many(item)


insert_data = Mongo_Client()