def solution(str1, str2):
    list1=[]
    list2=[]
    temp1=[] #합집합용
    temp2=[] #합집합용
    for i in range(0,len(str1)-1):
        if (ord(str1[i].lower())>= ord('a') and ord(str1[i].lower())<=ord('z')) and (ord(str1[i+1].lower())>= ord('a') and ord(str1[i+1].lower())<=ord('z')) :
            list1.append(str1[i].lower()+str1[i+1].lower())
            temp1.append(str1[i].lower()+str1[i+1].lower())
    for i in range(0,len(str2)-1):
        if (ord(str2[i].lower())>= ord('a') and ord(str2[i].lower())<=ord('z')) and (ord(str2[i+1].lower())>= ord('a') and ord(str2[i+1].lower())<=ord('z')):
            list2.append(str2[i].lower()+str2[i+1].lower())
            temp2.append(str2[i].lower()+str2[i+1].lower())

    print(list1)
    print(list2)
    result1=[]#합집합
    for i in temp1:
        result1.append(i)
        if i in temp2:
            temp2.remove(i)
    for i in temp2:
        result1.append(i)
    result2=[]#교집합
    if len(list1)>len(list2):
        for i in list2:
            if i in list1: # list2값이 list1에 있으면 교집합에 넣음
                result2.append(i)
                list1.remove(i)
    else:
        for i in list1:
            if i in list2: # list2값이 list1에 있으면 교집합에 넣음
                result2.append(i)
                list2.remove(i)
    print("합집합:",result1)
    print("교집합:",result2)
    if len(result1) ==0 and len(result2)==0:
        answer=65536
    else:
        answer = int(len(result2)/len(result1)*65536)
    
    return answer
