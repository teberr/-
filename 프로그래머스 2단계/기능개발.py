def solution(progresses, speeds):
    answer = []
    while len(progresses)!=0:
        count=0
        for i in range(0,len(progresses)):
            progresses[i]+=speeds[i]
            
        if progresses[0]>=100:
            count+=1
            for i in range(1,len(progresses)):
                if progresses[i]>=100:
                    count+=1
                else:
                    break
        if count!=0:
            answer.append(count)
            progresses=progresses[count:]
            speeds=speeds[count:]
        
    return answer
