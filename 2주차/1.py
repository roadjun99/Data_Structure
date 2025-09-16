value = int(input("연봉을 입력하세요 ==> "))
result = 0
firstValue = value

if value > 1200:
    result += 1200 * 0.06
    value -= 1200

else:
    result += value * 0.06
    value = 0

if value > 0:
    if value > 3400:
        result += 3400 * 0.15
        value -= 3400
    
    else:
        result += value * 0.15
        value = 0

if value > 0:
    if value > 4200:
        result += 4200 * 0.24
        value -= 4200
    
    else:
        result += value * 0.24
        value = 0

if value > 0:
    if value > 6200:
        result += 6200 * 0.35
        value -= 6200
    
    else:
        result += value * 0.35
        value = 0

if value > 0:
    result += value * 0.38
    value = 0

print('전체세금 = ', result)
print('순수소득 = ', firstValue - result)