def arithmetic_arranger(problems, show_answers=False ):
    
    #deben de ser solo 5 problemas
    if len(problems)>5:
        return'Error: Too many problems'

    #solo se pueden los operandos + y -
    for problem in problems:
        parts =problem.split()
        if parts[1] not in ['+','-']:
             return "Error: Operator must be '+' or '-'."
         
        #solo permite digitos
        if parts[0].isdigit()==False or parts[2].isdigit()==False:
            return 'Error: Numbers must only contain digits.'
        
        #maximo 4 digitos
        if len(parts[0])>4 or len(parts[2])>4:
            return 'Error: Numbers cannot be more than four digits.'

    #regresa la lista original
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')