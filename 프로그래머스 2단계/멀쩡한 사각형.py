import math
    
def solution(w,h):
    ratio=min(w,h)/max(w,h)
    w_c=w//math.gcd(w,h)
    h_c=h//math.gcd(w,h)
    answer=w*h-((max(w_c,h_c)-(max(w_c,h_c)*ratio-1))+(max(w_c,h_c)*ratio-1)*2)*math.gcd(w,h)
    # 총 개수 - (타일 1개만 지나는 경우+(타일 2개를 지나는 경우(=비율*가로 세로 중 큰거-1)))
    return answer
