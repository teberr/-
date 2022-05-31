import collections
dx=[0,-1,1,0]
dy=[-1,0,0,1]
def check(place):
    queue_P=collections.deque()
    queue=collections.deque()
    
    for i in range(0,len(place)):
        for j in range(0,len(place[0])):
            if place[i][j]=='P':
                queue_P.append([i,j])
    while queue_P:
        queue.append(queue_P.popleft())
        count=1
        visited=[[False]*5 for i in range(5)]
        sample_queue=collections.deque()
        while queue :
            #print("Queue의 상태:",queue)
            x1,y1=queue.popleft()
            visited[x1][y1]=True
            #print("탐색시작:",x1,y1)
            for x2,y2 in zip(dx,dy):
                if x1+x2<0 or x1+x2>4 or y1+y2 <0 or y1+y2>4 or visited[x1+x2][y1+y2]:
                    pass
                else:
                    if place[x1+x2][y1+y2]=='P': #거리가 2 이내에 다른 지원자가있다면 거짓
                        return 0
                    elif place[x1+x2][y1+y2]=='O' and count!=2: #거리가 1인점들은 한번 더 탐색해야 하므로 추가
                        sample_queue.append([x1+x2,y1+y2])
                        visited[x1+x2][y1+y2]==True
                    else:
                        pass
            if len(queue)==0 and count!=2: # 찾고자 하는 P지점에서 거리가 1인거 다 탐색하고 나면 거리 2인걸 탐색. 1인거에서 다탐색하면 거리 2인 점들은 더 탐색할필요없으므로 패스
                count+=1
                while sample_queue:
                    queue.append(sample_queue.pop())
                
        while queue:
            queue.pop()
    return 1
    
def solution(places):
    answer = []
    for x in places:
        answer.append(check(x))
    return answer
