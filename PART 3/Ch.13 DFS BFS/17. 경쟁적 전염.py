# # https://www.acmicpc.net/problem/18405

# # 내 풀이 시간초과 뜸

# # n, k = map(int,input().split())

# # board = [list(map(int,input().split())) for _ in range(n)]

# # s, x, y = map(int,input().split())

# # dx, dy = [0,1,0,-1], [1,0,-1,0]


# # def bfs(virus):
    
# #     worked = set()

# #     for i in range(n):
# #         for j in range(n):

# #             if board[i][j] == virus and (i,j) not in worked:

# #                 for z in range(4):

# #                     x,y = i+dx[z], j+dy[z]

# #                     if 0 <= x < n and 0 <= y < n:

# #                         if board[x][y] == 0:

# #                             board[x][y] = virus
# #                             worked.add((x,y))
                        
# # cnt = 0

# # while cnt < s:

# #     for i in range(1,k+1):
# #         bfs(i)

# #     cnt += 1

# # print(board[x-1][y-1] if board[x-1][y-1] != 0 else 0)

# # 정답

# from collections import deque
# n, k = map(int, input().split())

# graph = [] # 전체 보드 정보를 담는 리스트
# data = [] # 바이러스에 대한 정보를 담는 리스트

# for i in range(n):
#     # 보드 정보를 한 줄 단위로 입력
#     graph.append(list(map(int,input().split())))
#     for j in range(n):
#         if graph[i][j] != 0:
#             data.append((graph[i][j],0,i,j))

# data.sort()
# q= deque(data)

# target_s, target_x, target_y = map(int,input().split())

# dx, dy = [0,1,0,-1], [1,0,-1,0]

# while q:
#     virus, s, x, y = q.popleft()

#     if s == target_s:
#         break

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx and nx < n and 0 <= ny and ny < n:

#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s+1, nx, ny))

# print(graph[target_x - 1][target_y - 1])

from collections import deque

n, k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

s, x, y = map(int,input().split())

data = []

for i in range(n):
    for j in range(n):

        if board[i][j] != 0:
            data.append((board[i][j],0,i,j))

data.sort(key= lambda x : x[0])


def bfs(data):
    
    q = deque(data)

    dx = [-1, 0 , 1, 0]
    dy = [0, 1, 0, -1]

    while q:

        virus, ss, xx, yy = q.popleft()

        if ss == s:
            break

        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((board[nx][ny], ss + 1, nx, ny))

bfs(data)

# for i in board:
#     print(i)

print(board[x-1][y-1])


