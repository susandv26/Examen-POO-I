from pymongo import MongoClient
from classes import db_mongo
from classes import DATA, Dataprocess

def main():

    pipeline = Dataprocess()
    client, db = db_mongo.getDB()

    #Migrar careers
    #pipeline.migrar_datos(db, DATA)
    
    #careers
    #pipeline.create_careers(db, DATA)

    #course
    pipeline.create_courses(db, DATA)

    #students
    #pipeline.create_students(db, DATA)

    #enrollments

    #pipeline.create_enrollments(db, DATA)

    #datos = { 
    # 'cursos_aprobados': ['Química', 'Enfermería']
    #}

    #for i in range(len(datos["cursos_aprobados"])):
    #   aux = {'nombre': datos["cursos_aprobados"][i]}
    #   print(aux)


    return True

if __name__ == "__main__":
    main()