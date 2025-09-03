def pedir(voc):
    cont = 0
    
    for char in voc.lower():
        if char in 'aeiou':
            cont += 1
        elif not char.isalpha():
            print(f"'{char}' No es una vocal")
    return cont            
    
def main():
    cadena = input('Dame una palabra: ')
    total_voc=pedir(cadena)
    print("cantidad de vocales: ", total_voc)

main()