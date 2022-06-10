def solution(s):
    stack=[]
    for i in s:
        if i=="(":
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if len(stack)==0:

        return True
    else:
        return False
