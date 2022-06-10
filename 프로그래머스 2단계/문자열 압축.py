def solution(s):
    answer=len(s)
    #0 1 2 3 4 5 6  ->  012 345 6 (7) -> 3
    #0 1 2 3 4 5 6 7->  0123 4567 (8) -> 4
    for i in range(1,len(s)//2+1):
        count=1
        start=0
        end=len(s)-i
        temp=s
        result=[]
        result2=""
        while temp!="":
            result.append(temp[0:i])
            temp=temp[i:]
        #print(result)
        for i in range(0,len(result)-1):
            #print(result[i],result[i+1]) 
            if result[i]==result[i+1]:
                count+=1
            else:
                if count!=1:
                    result2=result2+(str(count)+result[i])
                    count=1
                else:
                    result2=result2+(result[i])
        if count!=1:
            result2=result2+(str(count)+result[i+1])
            count=1
        else:
            result2=result2+(result[i+1]) 
        answer=min(len(result2),answer)
        #print("result2",result2)
    #print(answer)
    return answer
