class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class Linkedlist:
    def __init__ ( self ):
        self.head = None
        self.size = 0

    def isEmpty( self ): return self.head == None

    def isFull( self ): return False

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : return None 
        else : return node.data

    def insert(self, pos, elem) :
        before = self. getNode(pos-1)
        if before == None :
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
        self.size += 1
        
    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :
            if self.head is not None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link

    def __len__(self) :
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.link
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.link

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.link
            current.link = prev
            prev = current
            current = next_node
        self.head = prev

class Polynomial:
    def __init__(self):
        self.arr = Linkedlist()

    def set(self):
        degree = int(input("최고 차항을 입력하세요: ")) + 1
        for i in range(degree):
            num = float(input(f"{degree - i - 1}차 항 입력: "))
            self.arr.insert(i, num)

    def cal(self, x):
        result = 0
        for i in range(len(self.arr)):
            num = self.arr.getEntry(i)
            for _ in range(len(self.arr) - i - 1):
                num *= x
            result += num
            print(f"{len(self.arr)-i-1}차 항: {num}")
        return result

    def add(self, p):
        result = Polynomial()
        len_self = len(self.arr)
        len_p = len(p.arr)
        max_len = max(len_self, len_p)

        a = list(self.arr)
        a.reverse()
        b = list(p.arr)
        b.reverse()
        c = Linkedlist()

        for i in range(max_len):
            coeff_self = a[i] if i < len_self else 0
            coeff_p = b[i] if i < len_p else 0
            c.insert(i, coeff_self + coeff_p)

        result.arr = c
        result.arr.reverse()
        return result

    def sub (self,p):
        return self.add(p.negate())

    def negate(self):
        result = Polynomial()
        result.arr = [-x for x in self.arr]
        return result


    def mult(self, p):
        result = Polynomial()
        a = list(self.arr)
        b = list(p.arr)
        temp = [0]*(len(a)+len(b)-1)

        for i in range(len(a)):
            for j in range(len(b)):
                temp[i+j] += a[i]*b[j]

        for v in temp:
            result.arr.insert(len(result.arr), v)
        return result

    def large_order(self) :
        return len(self.arr)-1

    def display(self):
        max_degree = len(self.arr) - 1
        terms = []

        for index, c in enumerate(self.arr):
            power = max_degree - index

            if c == 0:
                continue

            if power == 0:
                term = f"{c}"
            
            elif power == 1:
                term = f"{c}*x"
            
            else:
                term = f"{c}*x^{power}"

            terms.append(term)

        if not terms:
            print("0")

        else:
            expression = " + ".join(terms)
            expression = expression.replace("+ -", "- ")
            print(expression)

f = Polynomial()
g = Polynomial()

print("첫 번째 다항식 입력:")
f.set()

print("두 번째 다항식 입력:")
g.set()

print("첫 번째 다항식:")
f.display()

print("두 번째 다항식:")
g.display()

v = f.add(g)
print("두 개의 다항식의 합:")
v.display()

v = f.sub(g)
print("두 개의 다항식의 뺄셈:")
v.display()

z = f.mult(g)
print("두 개의 다항식의 곱:")
z.display()

x = float(input("대입할 수 입력: "))
print(f"다항식 f에 {x}을 대입한 결과 :{f.cal(x)}")
