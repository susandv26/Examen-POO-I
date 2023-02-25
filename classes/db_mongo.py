import pymongo

class db_mongo:
    
    @staticmethod
    def getDB():

        uri = "mongodb+srv://susan26:1234@supertech.ec1dut0.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        db = client['examen']

        print("exito")

        return client, db