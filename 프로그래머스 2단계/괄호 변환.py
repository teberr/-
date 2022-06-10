def correct(s):
    stack1=[]
    for x in s:
        if x=="(":
            stack1.append(x)
        else:
            if len(stack1)==0:
                return False
            else:
                stack1.pop()
    return True
        
def gal(s):
    
    count1=0
    count2=0
    u=""
    v=""
    result=""
    if s=="":
        return s
    else:
        for i in range(0,len(s)):
            if count1==count2 and count1!=0 :
                v=s[i:]
                break
            if s[i]=="(":
                u=u+s[i]
                count1+=1
            elif s[i]==")":
                u=u+s[i]
                count2+=1
    if correct(u)==True:
        v=gal(v)
    else:# ( u해놓은거 )+v
        result=result+"("
        result=result+gal(v)
        result=result+")"
        temp=u[1:-1]
        for x in temp:
            if x=="(":
                result=result+")"
            elif x==")":
                result=result+"("
            else:
                pass
        return result
    return u+v
                    
                
            
def solution(p):
    
        
    answer = gal(p)
    return answer
