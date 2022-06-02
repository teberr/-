def solution(n,a,b):
    answer = 0
    count=0
    temp=n
    while temp//2!=0:
        temp=temp//2
        count+=1
    start=0
    end=n
    while (start+end)//2!=start:
        mid=(start+end)//2
        if (a<=mid and b>mid) or (b<=mid and a>mid):
            break
        count-=1
        if a<=mid and b<=mid:
            end=mid
        if a>mid and b>mid:
            start=mid
    answer=count
    return answer
