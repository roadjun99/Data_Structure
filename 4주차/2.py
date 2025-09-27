class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, element):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = element
        
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            poppedElement = self.array[self.top]
            self.top -= 1
            return poppedElement
        
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        
        else:
            pass

def precedence(op):
    if op == '(' or op == ')':
        return 0
    
    elif op == '+' or op =='-':
        return 1
    
    elif op == '*' or op == '/':
        return 2
    
    else:
        return -1

def evalPostfix(expr):
    s = ArrayStack(100)

    for token in expr:
        if token in ['+', '-', '*', '/']:
            val2 = s.pop()            
            val1 = s.pop()            

            if token == '+':
                s.push(val1 + val2)
            
            elif token == '-':
                s.push(val1 - val2)
            
            elif token == '*':
                s.push(val1 * val2)

            elif token == '/':
                s.push(val1 / val2)

        else:
            s.push(float(token))

    return s.pop()


def infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()

                if op == '(':
                    break

                else:
                    output.append(op)


        elif term in ['+', '-', '*', '/']:
            while not s.isEmpty():
                op = s.peek()
                
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()

                else:
                    break

            s.push(term)

        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

infix1 = ['(','5','+','3', ')','*','3','-','1']
infix2 = ['(','4','-','8',')','*','4']

postfix1 = infix2Postfix(infix1)
postfix2 = infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)

print('중위표기: ', infix1)
print('후위표기: ', postfix1)
print('계산결과: ', result1, end = '\n\n')
print('중위표기: ', infix2)
print('후위표기: ', postfix2)
print('계산결과: ', result2)