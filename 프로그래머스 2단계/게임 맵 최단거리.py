import collections
dx=[1,0,0,-1]
dy=[0,1,-1,0]
def solution(maps):
    answer = 0
    queue=collections.deque()
    queue.append([0,0])
    row=len(maps)
    col=len(maps[0])

    while queue:
        x1,y1=queue.popleft()
        for x2,y2 in zip(dx,dy):
            if x1+x2<0 or x1+x2==row or y1+y2<0 or y1+y2==col or maps[x1+x2][y1+y2]==0:
                pass
            else:
                if maps[x1+x2][y1+y2]!=1 :
                    maps[x1+x2][y1+y2]=min(maps[x1+x2][y1+y2],maps[x1][y1]+1)
                else:
                    queue.append([x1+x2,y1+y2])
                    maps[x1+x2][y1+y2]=maps[x1][y1]+1

    if maps[row-1][col-1]==1:
        answer=-1
    else:
        answer=maps[row-1][col-1]
    return answer
