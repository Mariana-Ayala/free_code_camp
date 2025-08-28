def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    #creamos una funcion llamada raiz_cuadrada y le pasmos como parametros
    #num : al que se le sacara la raiz
    #tolerancia : diferencia aceptable entre el cuadrado delvalor aprox de la raiz
    #iterations : num de iteraciones a realizar 
    if square_target < 0: #si el numero es menor a 0
        raise ValueError('Square root of negative number is not defined in real numbers')
        #lanzamos un error porque no exixte raiz cuadrada de numeros negativos
        
    if square_target == 1: #si el numero es igual a 1
        root = 1
        print(f'The square root of {square_target} is 1')#la raiz es 1
        
    elif square_target == 0: #si el numero es igual a 0
        root = 0
        print(f'The square root of {square_target} is 0') #entonces el resultado es 0
        
    #si no es menor a 0, ni igual a 1 ni igual a 0 entonces 
    else:
        low = 0 #limite inferior lo inicializamos con 0
        high = max(1, square_target) ##limite superior, donde si el numero < 1 usamos como limite superior 1
        root = None #la variable root no tiene nada 
        
        for _ in range(max_iterations): #se crea un ciclo for
            #el cual queremos que se este repitiendo constantemente hasta M¿max_iterations = 100
            # colocamos "_" porque no nos importa el numero de indice
        
            mid = (low + high) / 2 #punto medio entere inferior y superior 
            square_mid = mid**2 #sacamos el cuadrado del punto medio

            if abs(square_mid - square_target) < tolerance: #checamos si el punto medio ya esta 
                #suficientemente cerca del numero 
                root = mid #root es igual al numero que seria la respuesta 
                break #y aqui se termina porque esa seria la respuesta de la raiz
            #ya que encontramos una aproximacion muy cerca

            elif square_mid < square_target: #si el medio al cuadrado es menor que el numero
                low = mid
                #la raiz se queda en la parte superior
            else: 
                high = mid #si no entonnces la raiz esta en la parte inferior 

        if root is None: #significa que no alcnazamos la tolerancia dentro de max_iterations
            print(f"Failed to converge within {max_iterations} iterations.")
            #si root se queda en None, es que no se lograron hacer las iteraciones
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
            #si si, entonces se da el resultado
    
    return root #se retorna en root para que se guarde el valor y se vuelva a ocupar para lo de las 
        #iteraciones

N = float(input('Ingrese numero para raiz: '))
square_root_bisection(N)