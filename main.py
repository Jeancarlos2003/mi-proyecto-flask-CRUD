from flask import Flask, render_template, jsonify, request

# Datos iniciales
carros = [
    {"id": "1", "marca": "Mazda", "modelo": 1983},
    {"id": "2", "marca": "Honda", "modelo": 1993},
    {"id": "3", "marca": "Toyota", "modelo": 2005},
    {"id": "4", "marca": "Chevrolet", "modelo": 2010},
    {"id": "5", "marca": "Ford", "modelo": 2018},
    {"id": "6", "marca": "Nissan", "modelo": 2020}
]

usuarios = [
    {"id": "1", "nombre": "Juan Pérez", "edad": 30},
    {"id": "2", "nombre": "Ana Gómez", "edad": 25},
    {"id": "3", "nombre": "Luis Fernández", "edad": 28},
    {"id": "4", "nombre": "Carlos López", "edad": 35},
    {"id": "5", "nombre": "María Torres", "edad": 40}
]

app = Flask(__name__)

# Endpoints para carros
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/carros", methods=["GET"])
def get_carros():
    return jsonify(carros)

@app.route("/carros", methods=["POST"])
def post_carros():
    nuevo_carro = request.json
    carros.append(nuevo_carro)
    return "Nuevo carro creado"

@app.route("/carros/<id>", methods=["DELETE"])
def delete_carro(id):
    for car in carros:
        if car["id"] == id:
            carros.remove(car)
            return f"Carro con id {id} ha sido eliminado"
    return "ID no encontrado"

@app.route("/carros/<id>", methods=["PUT"])
def put_carro(id):
    nuevo_carro = request.json
    for car in carros:
        if car["id"] == id:
            index = carros.index(car)
            carros[index] = nuevo_carro
            return "Carro actualizado"
    return "Carro no encontrado"

# Endpoints para usuarios
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def post_usuarios():
    nuevo_usuario = request.json
    usuarios.append(nuevo_usuario)
    return "Nuevo usuario creado"

@app.route("/usuarios/<id>", methods=["DELETE"])
def delete_usuario(id):
    for user in usuarios:
        if user["id"] == id:
            usuarios.remove(user)
            return f"Usuario con id {id} ha sido eliminado"
    return "ID no encontrado"

@app.route("/usuarios/<id>", methods=["PUT"])
def put_usuario(id):
    nuevo_usuario = request.json
    for user in usuarios:
        if user["id"] == id:
            index = usuarios.index(user)
            usuarios[index] = nuevo_usuario
            return "Usuario actualizado"
    return "Usuario no encontrado"

if __name__ == "__main__":
    app.run(debug=True)
