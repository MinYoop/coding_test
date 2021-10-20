from collections import deque

N, M = map(int,input().split())

board = [list(map(int,input())) for _ in range(N)]

chk = [[0]*M for _ in range(N)]
d = [[0]*M for _ in range(N)]

dx, dy = [1,0,-1,0], [0,1,0,-1]

cnt = 0




def bfs(x,y):
    global cnt
    global d
    q = deque()
    q.append([x,y])
    d[x][y] = 1

    find = False

    while q:
        x = q.popleft()

        chk[x[0]][x[1]] = 1

        cnt += 1

        for i in range(4):
            a = x[0]+dx[i]
            b = x[1]+dy[i]

            if a == N-1 and b== M-1:
                d[a][b] = d[x[0]][x[1]] + 1   
                find = True
                break
            if 0 <= a < N and 0 <= b < M:
                if board[a][b] == 1 and chk[a][b] == 0:  
                    d[a][b] = d[x[0]][x[1]] + 1               
                    q.append([a,b]) 
        
        if find:
            break   

bfs(0,0)
print(d[N-1][M-1])

# # 2번째 풀이

# from collections import deque

# n, m = map(int,input().split())

# board = [list(map(int,input())) for _ in range(n)]
# chk = [[0] * m for _ in range(n)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def bfs():

#     global chk
    
#     q = deque()
#     chk[0][0] = 1
#     visited = [(0,0)]
    
#     q.append((0,0))
    
#     while q:

#         x, y = q.popleft()       

#         for i in range(4):
#             nextX = x + dx[i]
#             nextY = y + dy[i]

#             if 0 <= nextX < n and 0 <= nextY < m:
#                 if board[nextX][nextY] == 1 and (nextX, nextY) not in visited:
#                     visited.append((nextX,nextY))
#                     q.append((nextX,nextY))
#                     chk[nextX][nextY] = chk[x][y] + 1


# bfs()

# print(chk[n-1][m-1])





