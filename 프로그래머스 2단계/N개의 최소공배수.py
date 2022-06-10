import math
def solution(arr):
    while len(arr)>1:
        a=arr.pop()
        b=arr.pop()
        c=math.gcd(a,b)
        arr.append(int(max(a,b)/c)*min(a,b))
    answer=arr[0]
    return answer
