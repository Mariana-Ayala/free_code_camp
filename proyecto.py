def arithmetic_arranger(problems, show_answers=False ):
    
    #deben de ser solo 5 problemas
    if len(problems)>5:
        return'Error: Too many problems'

    #solo se pueden los operandos + y -
    else:
        for problem in problems:
            parts =problem.split()
            if parts[1] not in ['+','-']:
             return "Error: Operator must be '+' or '-'."
         
    #los digitos de los problemas deben de ser numeros 
        else:
            for number in problems:
                op=number.split()
                if op[0].isdigit()==False or op[2].isdigit()==False:
                    return 'Error: Numbers must only contain digits.'
    
    #que los numeros sean solo de 4 digitos no mas 
    if len(op[0])>4 or len(op[2])>4:
                return 'Error: Numbers cannot be more than four digits.'

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')