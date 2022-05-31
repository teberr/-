import itertools
def solution(n, k):
    person=[i+1 for i in range(n)]
    answer=[]
    
    while person:
        count=1
        flag=0
        for i in range(1,len(person)):
            count*=i
        while k>count:
            k=k-count
            flag+=1
        answer.append(person.pop(flag))

    return answer
