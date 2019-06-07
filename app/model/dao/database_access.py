from pymongo import MongoClient


class DatabasAccess:

    def __init__(self, host, port, data_base, collection):
        self.host = host
        self.port = port

        self.client = MongoClient(host, port)
        self.data_base = self.client[f'{data_base}']
        self.collection = self.data_base[f'{collection}']

    def insert_one(self, dictionary):
        object_id = self.collection.insert_one(dictionary).inserted_id

        return object_id

    def insert_many(self, dictionary_list):
        self.collection.insert_many(dictionary_list)

    def find_one(self):
        return self.collection.find_one()

    def find(self, filter_dictionary=None):
        pass

    def find_all(self):
        # return self.collection.find()
        data = []
        for i in self.collection.find():
            data.append(i)
        return data
