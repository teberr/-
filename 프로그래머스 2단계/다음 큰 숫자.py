def solution(n):
    answer = 0 
    k=str(bin(n))[2:]
    temp=1 
    first_num1=-1
    num1_combo=-1
    number=0
    for i in range(len(k)-1,-1,-1):
        if k[i]=='1':
            first_num1=temp 
            for j in range(i,-1,-1):
                if k[j]=='1':
                    num1_combo+=1
                else:
                    break
            break
        else:
            temp*=2 #뒤에서 처음만난 1의 값(이 값을 더해줄것임)
    
    number=2**num1_combo-1 # 뒤에서 부터 첫음 만난 1을 자리 올림해주고 나서 사라진 1의 개수만큼 나중에 더해줘야하는 숫자
    answer=n+number+temp 
    return answer
# 뒤에서부터 1을 찾음(index) 거기서 부터 연속적인 1의 개수찾음 => 111이면 2개
# 
