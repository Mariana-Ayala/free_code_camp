def convert_to_snake_case(pascal_or_camel_cased_string): #declaramos una funcion de snake case con un 
    #parametro

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    #todo lo que esta escrito es como si estuviera dentro de una sola linea de comando 
    #lo que hace es dentro de una lista se hara 
    #agregar un "_" antes de cada letra mayuscula 
    #despues se convertira en minuscula 
    #si la letra es mayuscula entoncces se agrega el "_" y se convierte en minuscula
    #si no entonces se agrega a la lista
    #todo esto para cada caracter en la cadena 

    return ''.join(snake_cased_char_list).strip('_')
    #se retorna en una lista que se covinerte en cadena eliminando los "_" del inicio y final
    
def main(): #definimos la funcion principal
    print(convert_to_snake_case('IAmAPascalCasedString'))#mandmos a imprimir nuestra funcion 
    #y con parametro lla frase de prueba 
    print(convert_to_snake_case('IAmAPascalCasedString'))
    print(convert_to_snake_case('camelCaseExample'))
    print(convert_to_snake_case('PascalCase'))
    
main() #mandamos a llamar a la funcion principal