import copy
import math
import os
import time

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

class CircularQueue : 
    def __init__(self, capacity = 10) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
    
    def isEmpty( self ) :
        return self.front == self.rear
    
    def isFull( self ) :
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue( self, item ) :
        if not self.isFull() :
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass
    
    def dequeue( self ) :
        if not self.isEmpty() :
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass

    def peek( self ) :
        if not self.isEmpty() :
            return self.array[ (self.front + 1) % self.capacity ]
        else : pass
        
class PriorityQueue :
    def __init__(self, capacity = 10) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
    
    def isEmpty( self ) : return self.size == 0

    def isFull( self ) : return self.size == self.capacity

    def enqueue( self, e ) :
        if not self.isFull() :
            self.array[self.size] = e
            self.size += 1

    def findMaxIndex( self ) :
        if self.isEmpty() : return -1
        highest = 0
        for i in range(1, self.size) : 
            if self.array[i][2] > self.array[highest][2] :
                highest = i
        return highest
    
    def dequeue( self ) :
        highest = self.findMaxIndex()
        if highest != -1 :
            self.size -= 1
            self.array[highest], self.array[self.size] = \
            self.array[self.size], self.array[highest]
            return self.array[self.size]
        
    def peek( self ) :
        highest = self.findMaxIndex()
        if highest != -1 :
            return self.array[highest]
        
    def __str__( self ) :
        return str(self.array[0:self.size])

def isValidPos(x, y) :
    if 0 <= x < MAZE_SIZE_x and 0 <= y < MAZE_SIZE_y :
        if map[y][x] == '0' or map[y][x] == 'x' :
            return True
    return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def DFS(map) :
    stack = ArrayStack(100)
    stack.push((0,1))

    while not stack.isEmpty() :
        clear_screen()
        here = stack.pop()
        (x,y) = here
        drawMaze(map)
        print("현재 위치 :", here)
        print()
        time.sleep(0.5)

        if (map[y][x] == 'x') :
            map[y][x] = '.'
            clear_screen()
            drawMaze(map)
            print("미로탈출 성공")
            print("현재 위치 :", here)
            return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : stack.push(( x, y - 1)) # 상
            if isValidPos(x, y + 1) : stack.push(( x, y + 1)) # 하
            if isValidPos(x - 1, y) : stack.push(( x - 1, y)) # 좌
            if isValidPos(x + 1, y) : stack.push(( x + 1, y)) # 우

    return False

def BFS(map) :
    que = CircularQueue(100)
    que.enqueue((0, 1))
    
    while not que.isEmpty() :
        clear_screen()
        here = que.dequeue()
        (x,y) = here
        drawMaze(map)
        print("현재 위치 :", here)
        print()
        time.sleep(0.5)

        if (map[y][x] == 'x') : 
            map[y][x] = '.'
            clear_screen()
            drawMaze(map)
            print("현재 위치 :", here)
            print("탈출 성공")
            print()
            return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : que.enqueue(( x, y - 1)) # 상
            if isValidPos(x, y + 1) : que.enqueue(( x, y + 1)) # 하
            if isValidPos(x - 1, y) : que.enqueue(( x - 1, y)) # 좌
            if isValidPos(x + 1, y) : que.enqueue(( x + 1, y)) # 우
    return False

def MySmartSearch(map) :
    q = PriorityQueue()
    q.enqueue((0, 1,-dist(0, 1)))

    while not q.isEmpty():
        clear_screen()
        here = q.dequeue()
        x,y,_ = here
        drawMaze(map)
        print("현재 위치 :", here[0:2])
        print()
        time.sleep(0.5)

        if (map[y][x] == 'x') : 
            map[y][x] = '.'
            clear_screen()
            drawMaze(map)
            print("현재 위치 :", here[0:2])
            print("탈출 성공!")
            print()
            return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : q.enqueue(( x, y - 1, -dist(x, y - 1))) # 상
            if isValidPos(x, y + 1) : q.enqueue(( x, y + 1, -dist(x, y + 1))) # 하
            if isValidPos(x - 1, y) : q.enqueue(( x - 1, y, -dist(x - 1, y))) # 좌
            if isValidPos(x + 1, y) : q.enqueue(( x + 1, y, -dist(x + 1, y))) # 우
    return False

def dist(x, y) :
    (dx, dy) = (10 - x, 9 -y)
    return math.sqrt(dx*dx + dy*dy)

def drawMaze(map) :
    for row in map :
        for col in row :
            if col == '1' : print('■',end=' ')
            elif col == '0' : print(' ',end=' ')
            elif col == 'e' or col == 'x' : print('→',end=' ')
            elif col == '.' : print('√',end=' ')
        print()


org = [ 
[ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 
[ 'e', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
[ '1', '0', '0', '0', '1', '0', '1', '1', '0', '1', '0', '1'],
[ '1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '0', '1'],
[ '1', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1'],
[ '1', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '1'],
[ '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', 'x'],
[ '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '1'],
[ '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '1'],
[ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

MAZE_SIZE_x = 12
MAZE_SIZE_y = 10

clear_screen()

while True :
    drawMaze(org)
    select = input("탐색 방법 : 1 = DFS,  2 = BFS,  3 = PQueue,  q = 종료 ==> ")
    
    map = copy.deepcopy(org)
    if select == '1' :
        if not DFS(map) :
            print("미로 탈출 실패")

    elif select == '2' :
        if not BFS(map) :
            print("미로 탈출 실패")
    
    elif select == '3' :
        if not MySmartSearch(map) :
            print("미로 탈출 실패")

    elif select == 'q' :
        break

    else :
        print("입력 오류")