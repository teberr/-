def n_c(n,i):#n진법, 숫자i
    number="0123456789ABCDEF"
    a,b=i//n,i%n
    if a>=n:
        return n_c(n,a)+number[b] # 0
    else:
        if a!=0:
            return number[a]+number[b]
        else:
            return number[b]
def solution(n, t, m, p):
    index=[] # 3명 4개 2번째 순서 2,5,8,11
    numbers=[]
    for i in range(0,t):
        index.append(p+i*m)
   # print(index)
    answer = ''
    count=1
    for i in range(0,t*m):
        a=n_c(n,i)
        while a:
            numbers.append(a[0])
            a=a[1:]
   # print(numbers)
    for i in index:
        answer+=numbers[i-1]
    return answer
