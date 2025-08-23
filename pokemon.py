import requests #es para hacer peticiones en HTTP

def datos():
    pokemon = input("Escribe el nombre del pokemon: ").lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    if response.status_code == 200:  # 200 = Todo bien y guarda la respuesta que devuelve la API
        data = response.json()  # convierte los datos a tipo diccionario de python 
        print("Nombre:", data["name"])
        print("Altura:", data["height"])
        print("Peso:", data["weight"])
        print("Habilidades:")
        for ability in data["abilities"]: #recorre la lista de habilidades y las imprime una a una
            print("-", ability["ability"]["name"])
    else:
        print("Error en la petición:", response.status_code)

def nombres():
    cant = input("Cuantos pokemones quieres: ")
    url = f"https://pokeapi.co/api/v2/pokemon?limit={cant}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print ("Nombre de pokemon: ")
        num = 1
        for p in data["results"]:
            print (num, p["name"])
            num += 1
    else:
        print("Error al obtener la lista ")
    
def habilidades ():
        url = "https://pokeapi.co/api/v2/ability?limit=100"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Habilidades existentes: ")
            num = 1
            for ability in data["results"]:
                print(num, ability["name"])
                num += 1
        else:
            print("Error al obtener la lista")
            
def main():
    
    while True:
        print("1. Mostrar todos los datos de un pokemon")
        print("2. Mostrar todos los nombres de los pokemones")
        print("3. Mostrar todas las habilidades de los pokemones")
        print("4. Salir")
        
        opc = input("Que opcion eliges: ")
        
        if opc == "1":
            datos()
        elif opc == "2":
            nombres()
        elif opc == "3":
            habilidades()
        elif opc == "4":
            print("Saliendo del programa")
            break
main ()