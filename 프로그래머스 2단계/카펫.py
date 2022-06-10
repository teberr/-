def solution(brown, yellow):
    answer = []
    for i in range(1,int(yellow**(0.5))+1):
        if yellow%i==0:
            if brown==(yellow//i)*2+i*2+4:
                answer.append((yellow//i)+2)
                answer.append(i+2)
                break
    return answer
