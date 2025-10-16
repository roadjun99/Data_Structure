class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack :
    def __init__(self) :
        self.top = None

    def isEmpty(self) : return self.top == None

    def isFull(self) : return False

    def push(self, e) :
        self.top = Node(e, self.top)

    def pop(self) : 
        if not self.isEmpty():  
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.top.data 
        
def checkBrackets(data): 
    stack = LinkedStack()
    stackIndex = LinkedStack()
    lineNumber = 1

    for line in data.splitlines(): 
        charIndex = 1  
        
        for character in line:
            if character =='{' or character == '[' or character == '(' :
                stack.push(character)
                stackIndex.push((lineNumber, charIndex))

            elif character =='}' or character == ']' or character == ')':
                if stack.isEmpty():
                    print(f"오류 발생: 닫는 괄호 '{character}'에 대응하는 여는 괄호가 없습니다.")
                    print(f"오류 발생 위치: 파일의 {lineNumber}번째 라인, {charIndex}번째 문자")
                    return 
                
                left = stack.pop()
                leftLine, leftChar = stackIndex.pop()

                if (character == "}" and left != "{") or \
                   (character == "]" and left != "[") or \
                   (character == ")" and left != "("):
                    print(f"오류 발생: 괄호 쌍이 일치하지 않습니다")
                    print(f"오류 발생 위치: 파일의 {lineNumber}번째 라인 {charIndex}번째 문자")
                    return 2
            
            charIndex += 1
        lineNumber += 1

    if not stack.isEmpty():
        left = stack.pop()
        leftLine, leftChar = stackIndex.pop()
        print(f"오류 발생: 여는 괄호 '{left}'에 대응하는 닫는 괄호가 없습니다.")
        print(f"오류 발생 위치: 파일의 {leftLine}번째 라인, {leftChar}번째 문자")
        return 3

    print("오류가 발생하지 않았습니다")
    return 0

file = open("C:/Users/sm222/OneDrive/바탕 화면/이것이 코딩테스트다 알고리즘 유형별 기출문제/Q1.py", "r", encoding="utf-8")
fileData = file.read()
file.close()

file2 = open("C:/Users/sm222/OneDrive/바탕 화면/이것이 코딩테스트다 알고리즘 유형별 기출문제/Q2.py", "r", encoding="utf-8")
fileData2 = file2.read()
file2.close()

print("Q1.py 괄호 쌍 일치 불일치 결과 : ")
checkBrackets(fileData)
print()

print("Q2.py 괄호 쌍 일치 불일치 결과 : ")
checkBrackets(fileData2)