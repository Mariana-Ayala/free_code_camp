from flask import Flask, request, jsonify

postapp = Flask(__name__)

@postapp.route("/usuario", methods=["POST"])

def crear_usuario():
    datos = request.json
    #request todo lo que envia el cliente 
    #.json etrae los datos en formato json
        
    nombre = datos.get("nombre","desconocido")
    edad = datos.get("edad","no indicada")
    
    respuesta = {
        "mensaje":f"Hola {nombre}, tu edad es {edad}. Bienvenido a la API"
    }
    return jsonify(respuesta)

if __name__ == "__main__":
    postapp.run(debug=True)