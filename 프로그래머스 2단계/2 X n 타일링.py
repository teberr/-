def solution(n):
    result=[0,1,2,3]
    while n>=len(result):
        result.append((result[-1]+result[-2])%1000000007)
    

    return result[n]

# n result
# 1 1
# 2 2
# 3 3
# 4 (n-1)+(n-2)
# 5
