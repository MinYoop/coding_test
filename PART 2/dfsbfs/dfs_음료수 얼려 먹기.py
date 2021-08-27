

N, M = map(int,input().split())

board = [list(map(int,input())) for _ in range(N)]

chk = [[0]*M for _ in range(N)]

dx, dy = [1,0,-1,0], [0,1,0,-1]

cnt = 0

def dfs(x,y):
    global chk
    chk[x][y] = 1
    for i in range(4):

        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:

            if board[x+dx[i]][y+dy[i]] == 0 and chk[x+dx[i]][y+dy[i]] == 0:
                dfs(x+dx[i],y+dy[i])

for i in range(N):
    for j in range(M):

        if board[i][j] == 0 and chk[i][j] == 0:
            dfs(i,j)
            cnt += 1
            
print(cnt)

