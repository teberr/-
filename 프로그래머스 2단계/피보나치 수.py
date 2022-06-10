def solution(n):
    fibo=[0,1]
    while len(fibo)<=n:
        fibo.append(fibo[-1]+fibo[-2])
    answer=fibo[n]%1234567
    return answer
