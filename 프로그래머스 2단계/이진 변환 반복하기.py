def solution(s):
    answer = []
    count_0=0
    count_rep=0
    while s!='1':
        temp=''
        for i in range(0,len(s)):
            if s[i]=='1':
                temp=temp+s[i]
            else:
                count_0+=1
        count_rep+=1
        s=bin(len(temp))[2:]
    answer.append(count_rep)
    answer.append(count_0)
    return answer
