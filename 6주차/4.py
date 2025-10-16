import os,time,copy

class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__ ( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.rear == None 
    def isFull( self ): return False
   
    def deleteRear ( self ):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
        
    def addRear( self, item ):
        node = DNode(item, self.rear, None)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def addFront( self, item ):
        node = DNode(item, None, self.front)
        if( self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    def deleteFront( self ):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front==None:
                self.rear = None
            else:
                self.front.perv = None
        return data

def DFS(map) :
    stack = DoublyLinkedDeque()
    stack.addRear((0,1))

    while not stack.isEmpty() :
        clear_screen()
        here = stack.deleteRear()
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
            if isValidPos(x, y - 1) : stack.addRear(( x, y - 1)) # 상
            if isValidPos(x, y + 1) : stack.addRear(( x, y + 1)) # 하
            if isValidPos(x - 1, y) : stack.addRear(( x - 1, y)) # 좌
            if isValidPos(x + 1, y) : stack.addRear(( x + 1, y)) # 우

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

MAZE_SIZE_x = 12
MAZE_SIZE_y = 10
map = copy.deepcopy(org)

clear_screen()

if not DFS(map) :
    print("미로 탈출 실패")