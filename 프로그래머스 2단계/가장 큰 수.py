def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x)*3,reverse=True)
    for i in range(0,len(numbers)):
        answer=answer+str(numbers[i])
    answer=str(int(answer))
    return answer
