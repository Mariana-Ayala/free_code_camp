my_list = [1, 2] #esto es una lista 

my_list.append(3) #esto es para agregar un elemento a la lista
#se agrega al final de la lista
print(my_list)

print(my_list[0])#aqui imprime solo el indice 0 de la lista

my_list[0] = 0 #aqui se cambia el valor del indice 0 al valor 0
print(my_list)

my_list.insert(1, 1) #aqui insertamos en el indice 1 de la lista el valor de 1
print(my_list)

my_list.pop() #eliminar elementos o la lista completa 
print(my_list)

test = lambda x: x * 2 #es un tipo de funcion 
# la x es el parametro que utilizara la funcion
# lo demas es lo que hara 
print(test(3)) #para mandarla a llamar es com funcion normal 

test = lambda x: x * 2
print(list(map(test, [2, 3, 5, 8]))) #aqui estamos llamando una nueva funcion map()
#esta funcion hace que se puedan juntar dos funciones, comp primer parametro debe ir la funcion 
#a ejecutar y el segundo argumento se pasa como en donde se ejecutara esa funcion 
#y para imrpimir la funcion map() debe estar dentro del argumento list()
print(sum(map(test, [2, 3, 5, 8]))) #si le pasamos la funcion sum, entonces como resultao 
#nos dara la suma de 4,6,10,16 que es 36 