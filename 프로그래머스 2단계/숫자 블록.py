import math
def solution(begin, end):
    answer = []

    
    for i in range(begin,end+1):
        flag=0
        for j in range(2,int(math.sqrt(i))+1):
            if i//j<=10000000:
                if i%j==0:
                    answer.append(i//j)
                    flag=1      
                    break
        if flag==0:
            if i==1:
                answer.append(0)
            else:
                answer.append(1)
    return answer
  
