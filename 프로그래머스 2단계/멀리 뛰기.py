def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result
def solution(n):
    num1=n%2
    num2=n//2
    answer = 0

    while num2>=0:
        answer+=(factorial(num1+num2)//factorial(num1)//factorial(num2))
        num2-=1
        num1+=2
        
    return answer%1234567
