class Students:
    
    def __init__(self, numero_cuenta, nombre_completo, edad, Id_carrera):
        self.numero_cuenta = numero_cuenta
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.Id_carrera = Id_carrera

    def get_dict_estudiane(db):

        collection = db["Students"]  
        estudiantes = collection.find()

        dict_students = {}
        for e in estudiantes:
            dict_students[e["nombre_completo"]] = e["_id"] 

        return dict_students