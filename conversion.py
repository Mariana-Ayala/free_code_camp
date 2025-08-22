def verify_card_number(card_number):   #definimos una funcion con un parametro (card_number)
    #card_number es una cadena 
    
    sum_of_odd_digits = 0   #agregamos una variable inicializada en 0
    
    card_number_reversed = card_number[::-1]   #creamos una variable y le pasamos card_number 
    #y que la invierta
                                                
    odd_digits = card_number_reversed[::2] #creamos otra variable y le pasamos la cadena invertida pero
    #tomara de dos en dos, emepzando desde el indice 0 
    #esta cadena contiene los impares de la cadena original
    
    for digit in odd_digits: #para cada digito en en la nueva cadena de odd_digits
        sum_of_odd_digits += int(digit) #va irlos agregando, pero como es cadena, se debe convertir 
        #a entero

    sum_of_even_digits = 0 #creamos una variable inicializada en 0
    even_digits = card_number_reversed[1::2] #creamos una variable que le vamos a pasar
    #la cadena invertida pero solo los numeros pares, emepzando desde el indice 1 y toma cada 2 numeroa 
    
    for digit in even_digits:  #para cada digito en la cadena even_digts
        number = int(digit) * 2 # se va a duplicar, pero de igual manera se debe convertir a entero
        if number >= 10: #si el numero de la cadena invertida de pares (even_digits) es mayor o = 10
            number = (number // 10) + (number % 10) # entonces se sumaran sus digitos 
            #ejemplo si es 12 se sumara 1+2 
            #para ello, para tomar el (1) es con (number //10) (primer digito)
            #para tomar el (2) es con (number % 10) (segundo digito)
        sum_of_even_digits += number #se van agregando a esta variable 
        
    total = sum_of_odd_digits + sum_of_even_digits #y se van a sumar 
    #los numeros de la cadena off_digits + los numeros de la cadena number
    print(total)
    return total % 10 == 0 #el total es un multiplo de 10
    #si si es multiplo de 10 returna True 
    #si no es multiplo de 10 returna False

def main():
    card_number = '4111-1111-4555-1141' #la cadena de caracteres
    card_translation = str.maketrans({'-': '', ' ': ''}) #crea una tabla de traducción para quitar 
    #guiones y espacios.
    translated_card_number = card_number.translate(card_translation) #.translate aplica esa tabla 
    #con los cambios

    if verify_card_number(translated_card_number):#aqui mandamos a llamar la funcion 
        #verify_card_number y como parametro pasamos la cadena ya cambiada
        print('VALID!') # si el return da true entonces es valido
    else:
        print('INVALID!') #si el retunr da flase entonces es invalido

main() #aqui se manda a traer la funcion main 