import json

# Definir una clase que represente a un usuario
class User:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

# Desarrollar una función que tome un objeto User como entrada y genere una representación serializada en JSON
def serializar_usuario(user):
    return json.dumps(user.__dict__)

usuario = User("Angel", 19, "Angel@Prueba.com")
json_usuario = serializar_usuario(usuario)
print("JSON serializado:", json_usuario)

# Crear una función que tome la representación serializada como entrada y reconstruya el objeto User original.
datos_usuario = json.loads(json_usuario)
print("Nombre:", datos_usuario["nombre"])
print("Edad:", datos_usuario["edad"])
print("Correo:", datos_usuario["correo"])
