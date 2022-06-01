def solution(n, left, right):
    answer = [ ]

    for i in range(left,right+1):
        temp=i//n
        if i%n<=temp:
            answer.append(1+temp)
        else:
            answer.append(i%n+1)

    return answer
  
#12345  01234
#22345  56789
#33345  
#44445
#55555
