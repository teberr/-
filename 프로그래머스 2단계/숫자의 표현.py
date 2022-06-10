def solution(n):
    answer = 0

    for x in range(n,0,-1):
        sum=0
        for y in range(x,0,-1):
            sum+=y
            if sum==n:
                answer+=1
                break
            if sum>n:
                break
    return answer
