def solution(n):
    tile=[3,11]
    answer=0
    a=n//2

    for i in range(2,a):
        temp=tile[i-1]*3+tile[i-1]-tile[i-2]
        tile.append(temp)
    answer=tile[a-1]
    return answer%1000000007

# 2 -> 3
# 4 -> 11 = 3 *3 +2   
# 6 -> 41 = 3*3*3 +2*3 +2*3 +2
# 8 -> 153 
