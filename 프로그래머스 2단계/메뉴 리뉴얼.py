import itertools

def solution(orders, course):
    # 각 손님이 주문한 조합 중 course로 짤 수 있는 조합을 찾자.
    # course첫번째 값이 2이면 2개짜리 조합을 찾자.
    
    answer = []
    for index in course:
        dict_order={}
        print("target:",index)
        for order in orders:
        #    print("order",order)
            temp=list(map(list,itertools.combinations(order,index)))
            for i in range(0,len(temp)):
                s=""
                for j in range(0,len(temp[i])):
                    temp[i].sort()
                    s=s+temp[i][j]
                temp[i]=s
                if s not in dict_order.keys():
                    dict_order[s]=1
                else:
                    dict_order[s]=dict_order[s]+1
       #     print(temp)
       #     print(dict_order)
        
        temp_dict=(sorted(dict_order.items(),key=lambda x:x[1],reverse=True))
        
        max=-1
        for i in temp_dict:
            if max==-1:
                max=i[1]
            if max!=i[1] or i[1]<2:
                break
            answer.append(i[0])
            max=i[1]

    answer.sort()
    return answer
