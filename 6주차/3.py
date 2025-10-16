import os,time,copy

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedQueue:
    def __init__( self ):
        self.tail = None

    def isEmpty( self ): return self.tail == None 

    def isFull( self ): return False
    
    def enqueue( self, item ):
        node = Node(item, None)
        if self.isEmpty() :
            self.tail = node
            node.link = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue( self ):
        if not self.isEmpty():
            data = self.tail.link.data
        if self.tail.link == self.tail:
            self.tail = None
        else:
            self.tail.link = self.tail.link.link
        return data

def BFS(map) :
    que = LinkedQueue()
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

def drawMaze(map) :
    for row in map :
        for col in row :
            if col == '1' : print('■',end=' ')
            elif col == '0' : print(' ',end=' ')
            elif col == 'e' or col == 'x' : print('→',end=' ')
            elif col == '.' : print('√',end=' ')
        print()

def isValidPos(x, y) :
    if 0 <= x < MAZE_SIZE_x and 0 <= y < MAZE_SIZE_y :
        if map[y][x] == '0' or map[y][x] == 'x' :
            return True
    return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

org = [ 
[ '1', '1', '1', '1', '1', '1'], 
[ 'e', '0', '1', '0', '0', '1'],
[ '1', '0', '0', '0', '1', '1'],
[ '1', '0', '1', '0', '1', '1'],
[ '1', '0', '1', '0', '1', '1'],
[ '1', '0', '1', '0', '1', '1'],
[ '1', '0', '1', '0', '1', '1'],
[ '1', '0', '1', '0', '1', '1'],
[ '1', '1', '1', '0', '0', '1'],
[ '1', '1', '1', 'x', '1', '1']
]

MAZE_SIZE_x = 6
MAZE_SIZE_y = 10

map = copy.deepcopy(org)

if not BFS(map) :
    print("미로 탈출 실패")