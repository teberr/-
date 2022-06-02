def solution(s):
    answer = []
    listed=s[2:-2].split("},{")
    x=sorted(listed,key=lambda x:len(x))
    result=[]
    for i in x:
        result.append(list(map(int,i.split(','))))
    for i in result:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
    
    return answer
