# 테스트 케이스 톨아가는데 런타임에러뜬다..
# from copy import deepcopy
# from collections import deque

# n,m = map(int,input().split())
# nm = n*m
# board = [list(map(int,input().split())) for _ in range(n)]

# result = 0
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def count0(board):
#     cnt = 0

#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == 0:
#                 cnt+=1

#     # if cnt > 20:
#     #     print("보드상태")
#     #     for i in board:
#     #         print(i)

#     return cnt

# def virus(board):

#     visited = [[0] * m for _ in range(m)]
    
#     for i in range(n):
#         for j in range(m):

#             if board[i][j] == 2 and visited[i][j] == 0:
#                 q = deque()
#                 q.append((i,j))
#                 visited[i][j] = 1
#                 while q:                    
#                     a, b = q.popleft()
#                     for k in range(4):
#                         x, y = a+dx[k], b+dy[k]

#                         if 0 <= x < n and 0 <= y < m and visited[x][y] == 0 and board[x][y] == 0:
#                             q.append((x,y))
#                             visited[x][y] = 1
#                             board[x][y] = 2

#     return board    

# for i in range(nm-2):
#     ix = i // m
#     iy = i % m 

#     if board[ix][iy] != 0:
#         continue

#     for j in range(i+1,nm-1):
#         jx = j // m
#         jy = j % m 
#         if board[jx][jy] != 0:
#             continue

#         for z in range(j+1,nm):
#             zx = z // m
#             zy = z % m
#             if board[zx][zy] != 0:
#                 continue

#             board[ix][iy], board[jx][jy], board[zx][zy] = 1, 1, 1

#             copyBoard = virus(deepcopy(board))
            
#             result = max(result, count0(copyBoard))

#             board[ix][iy], board [jx][jy], board[zx][zy] = 0, 0, 0

# print(result)

# 아래도 백준에서 pypy로 돌려야 돌아간다

n, m = map(int, input().split())

data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def get_score():

    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        
        result = max(result, get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)