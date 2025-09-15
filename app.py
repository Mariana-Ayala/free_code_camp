from flask import Flask, request, jsonify
    #flask para crear api
    #reuest permite leer lo que nos envia el cliente 
    #jsonify convierte el direccionario de python a json para que api los devuelva al cliente 
app = Flask(__name__)
    #app creamos una aplicacion llamada app
    #__name__ es una variable 
@app.route("/edad", methods=["GET"])
    #generamos un endpoint llamado edad
    #desde donde el usuario hara las peticiones
        #donde pedir informacion o donde mandar datos 
    #el GET es solo enviarmos infrormacion pero no recibimos 
    #@app.route: un decorador cuando alguien viite \edad ejecuta la funcion de abajo
def home():
    #funcion
    nombre = request.args.get("nombre", "desconocido")  
    #request es el que contiene toda la informacion
    #args son los parametros en la url 
    #nombre,desconocido si encuentra un nombre lo guarda en la variable 
    #si no encuentra nada, lo guarda por defecto desconocido 
    return jsonify({
    "mensaje": f"Hola {nombre}, bienvenido a mi API!"
})

if __name__ == "__main__":

    #name sirve para ver en que modo se ejecutara


    #si se ejectua de manera directa name=main entonces ejecuta el servidor 
    #si se ejecuta de otra manera name="nombre del modulo" no arrancara el servidor 

    app.run(debug=True)
    #arranca el servidor web de Flask
    #debug activa el modulo de depuracion
    #se reinicia solo o muestra errores detallados 