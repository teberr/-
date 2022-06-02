def n_c(n,k):
    a,b=n//k,n%k
    s=str(b)
    while a>=k:
        a,b=a//k,a%k
        s=str(b)+s
    if a!=0:
        s=str(a)+s
    return s

def solution(n, k):
    answer = 0
    s=n_c(n,k)
    n_list=list(s.split('0'))
    for i in n_list:
        if i!='' and i!='1':
            flag=0
            for x in range(2,int(int(i)**(0.5))+1):
                if int(i)%x==0:
                    flag=1
                    break
            if flag==0:
                answer+=1

    return answer
