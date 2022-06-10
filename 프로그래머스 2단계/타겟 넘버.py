def target_number(numbers,target,i):
    answer=0
    sum=0
    if i==len(numbers):
        for j in range(0,len(numbers)):
            sum+=numbers[j]
        
        if sum==target:
            answer+=1

    else:
        answer+=target_number(numbers,target,i+1)
        numbers[i]=-numbers[i]
        answer+=target_number(numbers,target,i+1)

    return answer
def solution(numbers, target):
    answer=target_number(numbers,target,0)
    return answer
