def solution(s):
    
    answer=''
    s=s.lower()
    count=0
    for i in range(0,len(s)):
        if s[i]==" ":
            answer=answer+(s[i])
            count=0
        else:
            if count==0:
                answer=answer+(s[i].upper())
                count=1
            else:
                answer=answer+s[i]
    
    
    return answer
