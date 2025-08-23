import requests #es para hacer peticiones en HTTP

# Hacemos una petición GET a la API
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
