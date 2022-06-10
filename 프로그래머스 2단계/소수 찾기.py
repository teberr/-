import itertools

def string(numbers):
    string=[]
    for i in range(1,len(numbers)+1):
        a=list(map(list,itertools.permutations(numbers,i)))
        for x in a:
            s=""
            for k in range(0,len(x)):
                if len(s)==0:
                    if x[k]=='0':
                        pass
                    else:
                        s=s+x[k]
                else:
                    s=s+x[k]
            if s not in string and len(s)!=0:
                string.append(s)
    return string

def solution(numbers):
    numbers=sorted(numbers,reverse=True)
    s=""
    count=0
    for i in numbers:
        s=s+i
    prime=[0 for i in range(int(s)+1)]

    prime[0]=1
    prime[1]=1
    for i in range(2,len(prime)):
        if prime[i]==0:
            for j in range(i*2,len(prime),i):
                prime[j]=1
    number=string(numbers)
    for x in number:
        if prime[int(x)]==0:
            count=count+1
    answer = count
    return answer
