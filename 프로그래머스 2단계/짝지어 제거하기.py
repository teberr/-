def solution(s):
    answer = 0
    temp=[]
    for i in s:
        if len(temp)!=0 and temp[-1]==i:
            temp.pop()
        else:
            temp.append(i)
    if len(temp)==0:
        answer=1
    return answer
