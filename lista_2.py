def add_expense(expenses, amount, category): #funcion para agregar con 3 parametros (gastos, importe, categoria)
    expenses.append({'amount': amount, 'category': category}) #el .append es para agregar 
    
def print_expenses(expenses): #funcion para imprimir los gastos, con un parametro 
    for expense in expenses: #la variable gasto en gastos
        # para cada gasto en gastos se imprimira sus respectivos dtos 
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses): #funcion para mostrar el total, con un parametro
    return sum(map(lambda expense: expense['amount'], expenses)) 
    #sum es sumar todos los atributos que estan dentro 
    #map es para aplicar la accion en cada elemento 
    #lambda es un tipo de funcion breve 
    #todo esto se ira returnando 
    
def filter_expenses_by_category(expenses, category): #funcion para filtrar los gastos 
    return filter(lambda expense: expense['category'] == category, expenses)
    #filter pasa como primer argumento una funcion que lo es lambda y
    #como segundo argumento pasa algo iterable
    #filtrar es buscar, es decir, que buscara la categoria que se de, y mostrara todos
    #los datos que tengan esa categoria 
    

def main(): #aqui la funcion principal
    expenses = [] #una lista vacia de gastos 
    while True: #sea un ciclo infinito hasta que el usuario decida salor (5)
        print('\nExpense Tracker') #un tipo menu para poder escoger lo que se hara
        print('1. Add an expense') #agregar algun gasto
        print('2. List all expenses') #toda la lista de los gastos
        print('3. Show total expenses') #para ver todos los gastos con sus caracteristicas
        print('4. Filter expenses by category') #para filtrar no se que 
        print('5. Exit') #para salir del programa 
       
        choice = input('Enter your choice: ') #el imput lo que lee lo convierte a cadena    

        if choice == '1': #si la opcion es 1
            amount = float(input('Enter amount: ')) #que se coloque el importe
            category = input('Enter category: ') #que se coloque la categoria
            add_expense(expenses, amount, category) #se manda a llamar la funcion agregar y 
            #se agregan los nuevos datos

        elif choice == '2': #si la opcion es 2
            print('\nAll Expenses:') # se imprimen todos los datos
            print_expenses(expenses) #se manda a llamar la funcion para irmprimir 
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
            #aqui se imrpime solo todos los gastos, y se manda a llamar la funcion para el tota de
            #los gastos
    
        elif choice == '4':
            category = input('Enter category to filter: ') #se pide colocar la categoria a buscar
            print(f'\nExpenses for {category}:') 
            expenses_from_category = filter_expenses_by_category(expenses, category)
            #se crea una variable para pasarle la funcion de filtrar 
            print_expenses(expenses_from_category) #y se imprimen los datos de esa categoria 
    
        elif choice == '5':
            print('Exiting the program.')
            break
main()