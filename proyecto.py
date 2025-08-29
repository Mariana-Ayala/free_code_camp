def arithmetic_arranger(problems, show_answers=False ):
    
      #formato de impresion
    first_line = []
    second_line = []
    lines = []
    answer = []
    
    #deben de ser solo 5 problemas
    if len(problems)>5:
        return'Error: Too many problems'

    for problem in problems:
        op1, operator, op2 =problem.split()
        
        #solo se pueden operandos + y -
        if operator not in ['+','-']:
             return "Error: Operator must be '+' or '-'."
         
        #solo permite digitos
        if not (op1.isdigit() and op2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        #maximo 4 digitos
        if len(op1)>4 or len(op2)>4:
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(op1), len(op2)) + 2
        #numero de arriba alineado a la derecha
        first_line.append(op1.rjust(width))
        #numero de abajo alineado a la derecha
        second_line.append(operator + op2.rjust(width - 1))
        #guiones
        lines.append('-'*width)
        
        #si se piden las respuestas
        if show_answers:
            if operator == '+':
                result = str(int(op1)+int(op2))
            else:
                result = str(int(op1)-int(op2))
            answer.append(result.rjust(width))
        
    arranged = '    '.join(first_line)+'\n'+'    '.join(second_line)+'\n'+'    '.join(lines)
    if show_answers:
        arranged += '\n'+'    '.join(answer)
    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')