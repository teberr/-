def solution(record):
    id_nick={}
    chat=[]
    answer = []
    for i in record:
        temp=i.split()
        if len(temp)==3: # Enter,Change
            id_nick[temp[1]]=temp[2]
            chat.append([temp[0],temp[1]])
        else:#Leave
            chat.append([temp[0],temp[1]])

    for i in chat:
        if i[0]=="Enter":
            answer.append(id_nick[i[1]]+"님이 들어왔습니다.")
        elif i[0]=="Leave":
            answer.append(id_nick[i[1]]+"님이 나갔습니다.")
    
    
    return answer
