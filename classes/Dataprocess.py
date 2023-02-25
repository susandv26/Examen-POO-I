from classes.db_mongo import db_mongo
from classes.Careers import Careers

class Dataprocess:

    def _init_(self, data):
        self.__data = data

    def migrar_datos(self, db, datos):
        collection = db['data']
        collection.insert_many(datos)

    def create_careers(self, db, data):
        
        collection = db['Careers']

        for item in data:
            doc = { 'nombre': item['carrera']}
            collection.insert_one(doc)

    def create_courses(self, db, data):

        collection = db['Courses']

        #recolectar las clases de los cursos_aprobados
        for item in data:
            doc = { 'nombre': item['cursos_aprobados']}

            for i in range(len(doc["nombre"])):
                aux2 = { 'nombre': doc["nombre"][i]}
                collection.insert_one(aux2) 

        #recolectar las clases de los cursos_reprobados
        for item in data:
            doc = { 'nombre': item['cursos_reprobados']}

            for i in range(len(doc["nombre"])):
                aux2 = { 'nombre': doc["nombre"][i]}
                collection.insert_one(aux2)    

    def create_students(self, db, data):
        
        collection = db['Students']
        tipoCategoria = Careers.get_dict(db)
        
        for item in data:

           doc = {'numero_cuenta': item['numero_cuenta'], 'nombre_completo': item['nombre_completo'], 'edad': item['edad'], 'Id_carrera': tipoCategoria[item["carrera"]]}
           collection.insert_one(doc)
            
        
    def create_enrollments(self):
        pass