import sys
input = sys.stdin.readline

list1 = sorted(list(map(int, input().strip())), reverse=True)

count = list1[0]

for i in list1[1:]:
    if i <= 1 or count <= 1:
        count += i

    else:
        count *= i
    
print(count)