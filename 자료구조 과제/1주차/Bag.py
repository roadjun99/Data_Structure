# (1) 먼저 교재 코드 1.1, 1.2를 구현하고, 다양한 입력으로 테스트하라

def contains(bag, e):
    return e in bag

def insert(bag,e):
    bag.append(e)

def remove(bag,e):
    bag.remove(e)

def count(bag):
    return len(bag)

myBag = []

insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '손수건')
insert(myBag, '빗')
insert(myBag, '자료구조')
insert(myBag, '야구공')
insert(myBag, '금')
insert(myBag, '책')
print('가방속의 물건 : ', myBag)

insert(myBag, '빗')
remove(myBag, '손수건')
print('가방속의 물건 : ', myBag)

# (2) 23쪽의 도전 코딩 문제를 구현하고 테스트 코드를 작성하여 이 연산이 잘 동작하는 것을 보여라

def numOf(bag, e):
    if e in bag:
        return bag.count(e)
    else:
        return 0
    
print("빗의 개수 : ", numOf(myBag, '빗'))
print("책의 개수 : ", numOf(myBag, '책'))
print("손수건의 개수 : ", numOf(myBag, '손수건'))