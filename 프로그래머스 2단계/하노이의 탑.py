answer = []
def hanoi(fr,to,seq,i):
    if i==1:
        answer.append([fr,to])
    else:
        hanoi(fr,seq,to,i-1) # 시작점부터 중간점까지 마지막점을 거쳐서 i-1개를 옮김
        answer.append([fr,to])
        hanoi(seq,to,fr,i-1)

def solution(n):
    hanoi(1,3,2,n)
    return answer
