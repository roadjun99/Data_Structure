# (1) 연습문제 1.13을 구현하라. 피보나치 수열을 순환적인 방법과 
# 반복적인 방법으로 구하는 함수(fib(n), fib_iter(n))를 각각 작성하고, 
# 결과가 정상적으로 출력되는지 테스트한다
import time

n = int(input())

def fib(n):

    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fib(n-2) + fib(n-1)

def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[-1]

print(f"순환 : {fib(n)}")
print(f"반복 : {fib_iter(n)}")


#(2)  1번째부터 39번째까지의 피보나치 값을 구해보자.
# 즉 두 함수의 입력 으로 1~39를 전달하는 것이다 
# 각 함수의 처리 시간을 계산하여 출력하라 
# 이를 위해 24쪽의 코드와 설명을 참고하라

for n in range(1, 40):
    start_time = time.time()    
    a = fib(n)
    end_time = time.time() - start_time
    start_time = time.time()
    b = fib_iter(n)
    end_time2 = time.time() - start_time
    print(f"n = {n} 반복 : {end_time2}, 순환 : {end_time}")

