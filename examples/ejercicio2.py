def rev_pass(contra):
    hay_num = False
    hay_mayus = False
    
    for char in contra:
        if char.isdigit():
            hay_num = True
        if char.isupper():
            hay_mayus = True
    if len(contra) >= 8 and hay_mayus and hay_num:
        print ('Contraseña valida')  
    else:
        print('Contraseña invalida')


def main():
    contraseña = input('Dame una contraseña: ')
    contra_valid=rev_pass(contraseña)

main()