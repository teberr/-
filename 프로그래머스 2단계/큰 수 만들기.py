def solution(number, k):
    answer=[]
    for i in number:
        if len(answer)==0 or k==0:
            answer.append(i)
        else:
            while len(answer)>0 and k>0:  
                if answer[-1]<i:
                    answer.pop()
                    k=k-1
                else:
                    break
            answer.append(i)
    if k!=0:
        answer=answer[:-k]
    s=""
    for i in answer:
        s=s+i

    answer=s
    return answer
