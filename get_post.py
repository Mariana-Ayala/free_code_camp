from flask import Flask, request,jsonify
get_post = Flask(__name__)

#GET
#los datos vienen como parametros en la url
@get_post.route("/send", methods =["GET"])

def saludo():
    #el paramatro sera leido en la URL
    nombre=request.args.get("nombre", "desconocido")
    return jsonify({
        "mensaje": f"Hola {nombre},bienvenido a API GET"
    })
    
#POST
#para enviar datos dentro de body
@get_post.route("/receptor",methods = ["POST"])

def crear_usuario():
    datos = request.json
    nombre = datos.get("nombre", "desconocido")
    edad = datos.get("edad", "no indicada")
    return jsonify ({
        "mensaje" :f"Hola {nombre}, tu edad: {edad}, bienvenido a API POST"
    })

if (__name__ == "__main__"):
    get_post.run(debug=True)