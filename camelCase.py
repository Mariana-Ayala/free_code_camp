def convert_to_snake_case(pascal_or_camel_cased_string): #definimos una funcion con un parametro
    #funciona como pascalCase o Camel case 
    snake_cased_char_list = [] #colocamos una lista vacia
    #aqui vamos a guarda cada caracter convertido
    for char in pascal_or_camel_cased_string: #recorremos cada caracter de la cadena 
        if char.isupper(): #si la letra es mayuscula 
            converted_character = '_' + char.lower() #entonces se agregara un _ antes de cada mayuscula
            #y se convertira en minuscula 
            snake_cased_char_list.append(converted_character) #los agregamos a la lista 
        else: #si no es mayuscula
            snake_cased_char_list.append(char) # se agregara el caracter tal cual a la lista 
    snake_cased_string = ''.join(snake_cased_char_list) #se crea una nueva variable que 
    #con join una todas los carcateres en una sola cadena y no como lista 
    clean_snake_cased_string = snake_cased_string.strip('_') #creamos una nueva variable que contenga
    #elimine los "_" al inicio y alfinal de la cadena 

    return clean_snake_cased_string  #retornamos la cadena convertida 

def main(): #se crea un funcion principal
    print(convert_to_snake_case('aLongAndComplexString')) #mandamos a llamar a nuesta funcio anterior 
    #pasandole como parametro la frase que queremos 

main() #madamos a llamar nuestra funcion principal 
