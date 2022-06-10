from collections import deque
def solution(priorities, location):
    priorities=deque(priorities)
    answer=0
    count=1
    while len(priorities)!=0:
        while priorities[0]!=max(priorities):
            if location==0:
                location=len(priorities)-1
            else:
                location-=1
            priorities.append(priorities.popleft())
        
        if location==0:
            answer=count
            break
        else:
            priorities.popleft()
            location-=1
            count=count+1
        
    return answer
