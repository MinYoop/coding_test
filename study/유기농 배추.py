
from collections import deque

t = int(input())

def bfs(board, visited, i, j):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    q = deque()
    q.append((i,j))

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < len(board) and 0 <= yy < len(board[0]) and board[xx][yy] == 1 and visited[xx][yy] == 0:
                q.append((xx,yy))
                visited[xx][yy] = 1

results = []

for i in range(t):

    m, n, k = map(int,input().split())

    result = 0

    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        i, j = map(int,input().split())
        board[j][i] = 1
    
    for i in range(n):
        for j in range(m):

            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(board,visited,i,j)
                result += 1
    
    results.append(result)

for i in results:
    print(i)