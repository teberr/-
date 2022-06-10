def solution(arr1, arr2):
    answer = []
    for i in range(0,len(arr1)):
        temp=[]

        for j in range(0,len(arr2[0])):
            s=0
            for k in range(0,len(arr2)):
                s+=arr1[i][k]*arr2[k][j]     # 00 01 02           00 01
                                             # 10 11 12           10 11 
            temp.append(s)                   # 20 21 22           20 21
        answer.append(temp)

    return answer
# 00 01            00 01 02
# 10 11            10 11 12
# 20 21
