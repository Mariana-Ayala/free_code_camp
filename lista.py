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