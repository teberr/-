def solution(n):
    global answer
    answer=0
    graph=[[0 for i in range(n)]for i in range(n)]

    def isSafe(x,y):
        for i in range(0,y):
            if graph[x][i]==1:
                return False
        for i,j in zip(range(x,-1,-1),range(y,-1,-1)):
            if graph[i][j]==1:
                return False
        for i,j in zip(range(x,n),range(y,-1,-1)):
            if graph[i][j]==1:
                return False
        return True
            
    def backtracking(y,n):
        global answer
        if y==n:
            answer+=1
            return
        else:
            for x in range(0,n):
                if isSafe(x,y):
                    graph[x][y]=1
                    backtracking(y+1,n)
                    graph[x][y]=0
        return
    backtracking(0,n)
    return answer
