def solution(clothes):
    dict_clothes={}
    for i in clothes:
        for j in range(0,len(i)-1):
            if i[-1] not in dict_clothes.keys():
                dict_clothes[i[-1]]=[i[j]]
            else:
                dict_clothes[i[-1]].append(i[j])
    print(dict_clothes)
    answer = 1
    for key in dict_clothes.keys():
        answer=answer*(len(dict_clothes[key])+1)
    answer-=1
    return answer
