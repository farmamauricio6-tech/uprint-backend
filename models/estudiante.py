class Estudiante:
    def __init__(self, nombre, edad, id = None):
        self.nombre = nombre
        self.edad = edad
        self.id = id

    @classmethod
    def crear(cls, nombre, edad):
        # Code to insert a new student into the database
        pass

    @classmethod
    def obtener_todos(cls):
        # Code to retrieve all students from the database
        pass

    @classmethod
    def buscar_por_nombre(cls, nombre):
        # Code to search for students by name in the database
        pass

    @classmethod
    def obtener_por_id(cls, id):
        # Code to get a student by ID from the database
        pass
