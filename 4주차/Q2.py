import sys
input = sys.stdin.readline

list1 = sorted(list(map(int, input().strip())), reverse=True)

count = list1[0]

for i in list1[1:]:
    if i <= 1 or count <= 1:
        count += i

    else:
        count *= i
    
# ')'가 없기 때문에 오류 발생
print(count
