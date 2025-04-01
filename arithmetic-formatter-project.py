#There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
#Numbers should be right-aligned.

#operands a list of string numbers
#operator a string that represents operators (+ or -)
#answer is a string that contains the result

def formating_problem(operands, operator, answer):
    required_blank_space_size = 1
    operator_size = 1

    longest_operand = max(len(operands[0]), len(operands[1]))
    row_size = longest_operand + required_blank_space_size + operator_size
    padding_first_row = row_size - len(operands[0])
    padding_second_row = row_size - operator_size - len(operands[1])
    padding_fourth_row = row_size - len(answer)

    first_row = (' ' * padding_first_row) + operands[0]
    second_row = operator + (' ' * padding_second_row) + operands[1]
    third_row = ('-' * row_size)
    fourth_row = (' ' * padding_fourth_row) + answer

    #return '\n'.join([first_row, second_row, third_row, fourth_row]) 
    return [first_row, second_row, third_row, fourth_row]


#problem is the operation being evaluated which is a string

def parse_problem(problem):
    possible_operators = ['+', '-']
    operator = ''
    for char in problem:
        if char == possible_operators[0]:
            operator = char
            break
        
        elif char == possible_operators[1]:
            operator = char
            break
    
    if operator == '':
        raise Exception("Error: Operator must be '+' or '-'.")

    operands = problem.split(operator)
    operands[0] = operands[0].strip()
    operands[1] = operands[1].strip()

    for operand in operands:
        if not operand.isnumeric():
            raise Exception('Error: Numbers must only contain digits.')
        
        if len(operand) > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')

    
    
    return {'operands': operands, 'operator': operator}
    

def results(operands, operator):
    int_first_operand = int(operands[0])
    int_second_operand = int(operands[1])

    if operator == '+':
        answer = int_first_operand + int_second_operand
        return str(answer)
    
    elif operator == '-':
        answer = int_first_operand - int_second_operand
        return str(answer)


def arrange_problems(formatted, show_answers):
    row_count = 3
    if show_answers:
        row_count = 4

    rows = []
    for row_num in range(0, row_count):
        row = []
        for problem in formatted:
            #print(ftype(problem))
            row.append(problem[row_num])

        row_str = '    '.join(row)
        rows.append(row_str)
    
    return '\n'.join(rows)





def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return  'Error: Too many problems.'
    
    formatted = []
    for p in problems:

        try:
            problem = parse_problem(p)
        except Exception as err:
            return str(err)

        answer = results(problem['operands'], problem['operator'])
        problem_rows = formating_problem(problem['operands'], problem['operator'], answer)
        formatted.append(problem_rows)

    return arrange_problems(formatted, show_answers)



# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')   

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}') 
