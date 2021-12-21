from collections import deque

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

shark = 2
eated = 0 
sharkLoc = None

time = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sharkLoc = [i,j,0]
            board[i][j] = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(board):
    global shark
    global sharkLoc
    global eated
    visited = []

    q = deque()
    minLoc = 1e9
    q.append(sharkLoc)
    tmp = 0
    while q:

        locX, locY, time = q.popleft()
        visited.append([locX,locY])
        

        if board[locX][locY] < shark and board[locX][locY] != 0:
            eated += 1
            if eated == shark:
                eated = 0
                shark += 1

            board[locX][locY] = 0
            sharkLoc = [locX,locY,time]
            
            return time

        for i in range(4):
            x, y = locX + dx[i], locY + dy[i]

            if 0 <= x < n and 0 <= y < n  and board[x][y] <= shark:
                if [x,y] not in visited:
                    q.append([x,y,time+1])
    return 0




nothing = False

while not nothing:

    # print(shark,board)
    # print(sharkLoc)
    # print("-----------")
    
    
    tmpTime = bfs(board)
    
    if tmpTime == 0:
        nothing = True
    

    

print(sharkLoc[2])

