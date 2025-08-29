def arithmetic_arranger(problems, show_answers=False ):
    
    if len(problems)>5:
        return'Error: Too many problems'

    else:
        for problem in problems:
            parts =problem.split()
            if parts[1] not in ['+','-']:
             return "Error: Operator must be '+' or '-'."


    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')