from flask import Flask,request,jsonify

BD = Flask(__name__)

usuarios = {} #guardar los usuarios
@BD.route ("/BaseDatos", methods = (["POST"]))

def agregar_usuario():
    datos = request.json
    nombre = datos.get("nombre")
    edad = datos.get("edad")
    
    if not nombre or not edad:
        return jsonify({"mensaje": f"falta nombre o edad"}), 400
    
    usuarios [nombre] = edad 
    #guarda o actualiza los datos del usuario
    return jsonify({
        "mensaje":f"Usiario {nombre} se agrego o actualizo con edad {edad}"
    })
    
@BD.route ("/BaseDatos", methods = (["GET"]))

def consultar_usuario():
    nombre = request.args.get("nombre")
    if not nombre:
        return jsonify ({
            "mensaje":f"Debes enviar el nombre "
        }) , 400
    
    edad = usuarios.get(nombre)
    if edad is None:
        return jsonify ({
            "mensaje":f"Usuario {nombre} no encontrado "
        }) ,400
    return jsonify ({
        "nombre":nombre,
        "edad":edad
    })
    
if __name__ == "__main__":
    BD.run(debug=True)