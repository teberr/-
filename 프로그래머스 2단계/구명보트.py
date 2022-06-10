import collections
def solution(people, limit):
    people.sort(reverse=True)
    people=collections.deque(people)
    
    count=0
    while len(people)>1:
        a=people.popleft()
        b=people.pop()
        if a+b<=limit:
            count+=1
        else:
            people.append(b)
            count+=1
    if len(people)!=0:
        people.pop()
        count+=1

    answer = count
    return answer
