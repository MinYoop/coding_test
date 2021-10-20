

# N, M = map(int,input().split())

# board = [list(map(int,input())) for _ in range(N)]

# chk = [[0]*M for _ in range(N)]

# dx, dy = [1,0,-1,0], [0,1,0,-1]

# cnt = 0

# def dfs(x,y):
#     global chk
#     chk[x][y] = 1
#     for i in range(4):

#         if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:

#             if board[x+dx[i]][y+dy[i]] == 0 and chk[x+dx[i]][y+dy[i]] == 0:
#                 dfs(x+dx[i],y+dy[i])

# for i in range(N):
#     for j in range(M):

#         if board[i][j] == 0 and chk[i][j] == 0:
#             dfs(i,j)
#             cnt += 1
            
# print(cnt)



# 2번째 풀이
from collections import deque

n, m = map(int,input().split())

board = [list(map(int,list(input()))) for _ in range(n)]

chk = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(chk, x , y):

    chk[x][y] = 1

    for i in range(4):

        nextX = x + dx[i]
        nextY = y + dy[i]

        if 0 <= nextX < n and 0 <= nextY < m:
            if chk[nextX][nextY] == 0 and board[nextX][nextY] == 0:
                #chk[nextX][nextY] = 1
                dfs(chk, nextX, nextY)


def bfs(chk, x, y):

    q = deque()

    q.append((x,y))

    while q:

        x, y = q.popleft()

        for i in range(4):

            nextX = x + dx[i]
            nextY = y + dy[i]

            if 0 <= nextX < n and 0 <= nextY < m :
                if chk[nextX][nextY] == 0 and board[nextX][nextY] == 0:

                    chk[nextX][nextY] = 1
                    q.append((nextX,nextY))
                        

cnt = 0
for i in range(n):
    for j in range(m):

        if board[i][j] == 0 and chk[i][j] == 0:
            bfs(chk, i, j)
            cnt += 1
            


print(cnt)


    


