import random

min = 0
max = 99
ai = random.randint(min,max)

for i in range(1, 10+1):
    n = int(input(f"숫자를 입력하세요(범위:{min}~{max}): "))

    if ai == n:
        print(f"정답입니다. {i}번 만에 맞추셨습니다.")
        print("게임이 끝났습니다")
        break

    elif ai > n:
        print("아닙니다. 더 큰 숫자입니다!")
        min = n
    
    else:
        print("아닙니다. 더 작은 숫자입니다!")
        max = n

    if i == 10:
        print("게임이 끝났습니다")
        print(f"정답은 {ai}입니다")
        break