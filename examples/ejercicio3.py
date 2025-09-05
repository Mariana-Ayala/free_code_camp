def buscar(alum):
    alumnos = {"Antonio":7 , "Federico":6, "Fabiola":9}
    if alum in alumnos:
        print(f"Su calificacion es: {alumnos[alum]}")
    else:
        print("Estudiante no encontrado")


def main ():
    nom = input("Dame el nombre el nombre del alumno a buscar: ").title()
    
    buscar(nom)
    
main()
    
    