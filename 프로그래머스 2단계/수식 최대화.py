import itertools

def solution(expression):
    stack=[]
    expression_list=[]
    index=0
    for i in range(0,len(expression)):
        if (expression[i] =="-" or expression[i]=="*" or expression[i]=="+" ) :
            if expression[i] not in stack:
                stack.append(expression[i])
            expression_list.append(int(expression[index:i]))
            expression_list.append(expression[i])
            index=i+1
    expression_list.append(int(expression[index:]))
#    print("stack:",stack)
    
    temp=list(itertools.permutations(stack,len(stack)))
    operand_list=[]
    for i in temp:
        operand_list.append(list(i))
    print("expression_list:",expression_list)    
    print("operand_list:",operand_list) 
    m=0
    for op_list in operand_list: # 연산자 우선순위 조합 중 하나 가져옴
        expression=[]
        for i in expression_list:
            expression.append(i)
#        print("expression",expression,"op_list:",op_list)
        for op in op_list: # 연산자 우선순위 리스트에서 첫번째,두번째,세번째 가져옴
            while op in expression: # expression에 우선순위인 연산자가 있다면
                for k in range(0,len(expression)):#돌면서                 
                    if expression[k]==op: #연산자 계산 결과를 temp4에저장
                        if op=="+":
                            expression[k]=expression[k-1]+expression[k+1]
                            expression.pop(k+1)
                            expression.pop(k-1)
                            break
                        if op=="-":
                            expression[k]=expression[k-1]-expression[k+1]
                            expression.pop(k+1)
                            expression.pop(k-1)

                            break
                        if op=="*":
                            expression[k]=expression[k-1]*expression[k+1]
                            expression.pop(k+1)
                            expression.pop(k-1)
                            break
            if len(expression)==1:
                m=max(m,abs(expression[0]))
#            print(expression)           

    answer = m
    
    return answer
