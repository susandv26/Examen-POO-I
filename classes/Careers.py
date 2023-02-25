
class Careers:

    def __init__(self, nombre):
        self.nombre = nombre


    def get_dict(db):
        collection = db["Careers"]
        carreras = collection.find()

        dict_careers = {}
        for e in carreras:
            dict_careers[e["nombre"]] = e["_id"] 

        return dict_careers

    
        