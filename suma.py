from flask import Flask,request,jsonify

suma = Flask(__name__)

@suma.route ("/suma_post",methods = ["POST"])

def suma_post():
    datos = request.json
    
    #numero1 = datos.get("Numero 1", "no indicado")
    #numero2 = datos.get("Numero 2", "no indicado")
    
    numero1 = int(datos.get("numero1", 0))
    numero2 = int(datos.get("numero2",0))
    resul = numero1+numero2
    return jsonify ({
        "resultado" : f"El resultado de la suma: {numero1} + {numero2} es: {resul} "
    })

if (__name__ == "__main__"):
    suma.run(debug=True)

