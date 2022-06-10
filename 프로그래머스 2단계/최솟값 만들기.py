def solution(A,B):
    answer = 0
    C=[]
    A.sort(reverse=True)
    B.sort()
    for i in range(0,len(A)):
        C.append(A[i]*B[i])
    print(C)
    for i in C:
        answer+=i

    return answer
