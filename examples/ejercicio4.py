def buscar(fru):
    frutas = {"Manzana": 18, "Mango":25, "Uva":36}
    if fru in frutas:
        print(f"La fruta contiene: {frutas[fru]}")
        compra = input(f'Cuantas frutas quieres comprar: ')
        if compra.isdigit():
            if int(compra) > frutas[fru]:
                print("No hay suficientes en el almacen")
            else:
                total = frutas[fru] - int(compra)
                print(f"Quedan: {total} unidades")
        else:
            print("No es una cantidad")
    else: 
        print("fruta no existente")
    
def main():
    frut = input(f'Ingresa el nombre de la fruta: ').title()
    buscar(frut)

main()