def gal(string):
    stack=[]
    for i in range(0,len(string)):
        if string[i]=="(" or string[i]=="[" or string[i]=="{":
            stack.append(string[i])
        else:
            if string[i]==")":
                if len(stack)!=0:
                    if stack.pop()!="(":
                        return False
                else:
                    return False
            if string[i]=="]":
                if len(stack)!=0:
                    if stack.pop()!="[":
                        return False
                else:
                    return False            
            if string[i]=="}":
                if len(stack)!=0:
                    if stack.pop()!="{":
                        return False
                else:
                    return False
    if len(stack)==0:
        return True
def solution(s):
    count=0
    for i in range(0,len(s)):
        if gal(s)==True:
            count+=1    
        s=s[1:]+s[0]
    answer = count
    return answer
