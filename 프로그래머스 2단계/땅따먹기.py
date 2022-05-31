
def solution(land):
    answer = 0


    for x in range(1,len(land)):
        for i in range(0,4):
            temp=land[x][i]
            for j in range(0,4):
                if i!=j:                   
                    temp=max(temp,land[x-1][j]+land[x][i])
            land[x][i]=temp
    
    answer=max(land.pop())
    return answer
