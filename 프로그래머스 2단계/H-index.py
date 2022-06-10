def solution(citations):

    citations.sort(reverse=True)
    print(citations)
    answer=citations[0]
    flag=0
    while flag==0:
        count=0
        for i in range(0,len(citations)):
            if citations[i]>=answer:
                count+=1
            else:
                break
        print("answer:",answer,"count",count)
        if count>=answer:
            flag=1
            break
        answer-=1

    return answer
