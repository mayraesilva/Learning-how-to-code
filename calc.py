def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems'
    
    for operator in ["*", "/"]: #negative way
        if operator in ''.join(problems):
            return "Error: Operator must be '+' or '-'."
    
    for operation in problems: #as operations are elements of a list
        operators = ["+", "-"]
        for operator in operators:
            #print(operator)
            if not operator in operation:
                continue
            
            for operand in operation.split(operator): #using operators as separators 
                #print(operand)
                if not operand.strip().isnumeric():
                    return 'Error: Numbers must only contain digits.'
                elif len(operand.strip()) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
    
    #Passed conditions
        #Passed conditions
    
    for operation in problems:
        possible_operators = ["+", "-"]
        operands = []
        operator = ''
        
        for possible_operator in possible_operators:
            if not possible_operator in operation:
                continue
            
            operator = possible_operator
            
            for operand in operation.split(operator): #using the signs as separators
                operands.append(int(operand.strip()))
        
        max_length = max(len(str(operands[0])), len(str(operands[1])))
        for index, item in enumerate(operands):
            #print(str(x).rjust(max_length))
            print(index, item)
            ' ' + item[1]
            

        print()

                # print("operando", operand)
                # print("este é o segundo operando ", operand[+1]) #O PROBLEMA ESTÁ AQUI, ESTAMOS CONTANDO ERRADO
                # print("meio do teste")
                # temp_operand = operand.strip()
                # temp_operand_2 = operand[+1].strip()
                # print("este é o operando temporário segundo", temp_operand_2)
                # print("este é o operando temporário primeiro ", temp_operand)
                # longest_operand = max(temp_operand, temp_operand_2)
                # print("este é o maior operando", longest_operand)
                # print("Final do teste")
                # #PROBLEMA, O TESTE ESTÁ FINALIZANDO SEPARANDO A OPERAÇÃO
                #ACHO QUE ESTOU CONTANDO CARACTERES
                #O 32 CONTA COMO 32 E 2,MAS DEVERIA SER 32 E 698

            


                # """            
                #     #comparing sizes             
                #     if len(operand) >= len(operand[+1]):
                #     longest = len(operand)
                #     smaller = len(operand[+1])
                #     longest_operand = operand.rjust(1)
                #     smaller_operand = operand[+1].rjust((longest - smaller  + 1))
                #     test_to_see_if_true = len(longest_operand) == len(smaller_operand)
                #     print(test_to_see_if_true)
                #     print(longest_operand)
                #     print(smaller_operand)
                #     print("camilly")
                #     #print(smaller_operand)"
                # """
                
                




#print(f'\n{arithmetic_arranger(["32 + 698"])}') #print to visualize the result during testing
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')