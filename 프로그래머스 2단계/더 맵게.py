import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while scoville[0]<K and len(scoville)>1:
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+(b*2))
        count=count+1
    if scoville[0]>=K:
        answer = count
    else:
        answer=-1
    return answer
