def solution(rows, columns, queries):
    table=[]
    answer = []
    t=1
    for i in range(0,rows):
        temp=[]
        for j in range(0,columns):
            temp.append(t)
            t=t+1
        table.append(temp)
    
        
    for j in queries:
        x1,y1,x2,y2 = j[0]-1,j[1]-1,j[2]-1,j[3]-1
        #(1,1 ->1,3) (1,3 ->4,3) (4,3->1,3) (1,3->1,1)
        #  (x1,y1)-------(x1,y2)
        #     |             |
        #     |             |
        #  (x2,y1)-------(x2,y2)
        m=table[x1][y1]
        temp2=m
        for i in range(x1,x2): 
            table[i][y1],table[i+1][y1] = table[i+1][y1],table[i][y1]
            m=min(m,table[i][y1])
        #print("왼쪽 상단")
        #for i in table:
        #    print(i)
        for i in range(y1,y2):
            table[x2][i],table[x2][i+1]=table[x2][i+1],table[x2][i]
            m=min(table[x2][i],m)
        #print("아래")
        #for i in table:
        #    print(i)        
        for i in range(x2,x1,-1):
            table[i][y2],table[i-1][y2]=table[i-1][y2],table[i][y2]
            m=min(table[i][y2],m)
        #print("오른쪽")
        #for i in table:
        #    print(i)
        for i in range(y2,y1+1,-1):
            table[x1][i],table[x1][i-1]=table[x1][i-1],table[x1][i]
            m=min(table[x1][i],m)
        #print("위")
        #for i in table:
        #    print(i)
        
        answer.append(m)
        
    return answer
