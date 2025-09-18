class Polynomial:
    def __init__(self):
        self.arr = []

    def set(self):
        degree = int(input("최고 차항을 입력하세요: ")) + 1
        for i in range(degree):
            self.arr.append(float(input(f"{degree - i - 1}차 항 입력: ")))

    def cal(self, x):
        result = 0
        for i in range(len(self.arr)):
            num = self.arr[i]
            for _ in range(len(self.arr) - i - 1):
                num *= x
            result += num

        return result

    def add(self, p):
        result = Polynomial()
        len_self = len(self.arr)
        len_p = len(p.arr)
        
        max_len = max(len_self, len_p)
        a = [0] * (max_len - len_self) + self.arr
        b = [0] * (max_len - len_p) + p.arr
        result.arr = [a[i] + b[i] for i in range(max_len)]

        return result

    def sub(self, p):
        return self.add(p.negate())

    def negate(self):
        result = Polynomial()
        result.arr = [-x for x in self.arr]

        return result

    def mult(self, p):
        result = Polynomial()
        result.arr = [0] * (len(self.arr) + len(p.arr) - 1)

        for i in range(len(self.arr)):
            for j in range(len(p.arr)):
                result.arr[i + j] += self.arr[i] * p.arr[j]

        return result

    def degree(self):
        return len(self.arr) - 1

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

print(f"f의 최고차수: {f.degree()}")

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
print(f"다항식 f에 {x}을 대입한 결과: {f.cal(x)}")