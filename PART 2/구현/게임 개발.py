# N, M = map(int, input().split())

# d = [[0] * M for _ in range(N)]

# x,y, direction = map(int, input().split())

# d[x][y] = 1

# array = []

# for i in range(N):
#     array.append(list(map(int,input().split())))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# count = 1

# turn_time = 0
# while True:
#     turn_left()

#     nx = x + dx[direction]
#     ny = y + dy[direction]

#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         x = nx
#         y = ny

#         count += 1
#         d[x][y] = 1
#         turn_time = 0
#         continue
#     else:
#         turn_time+=1
    
#     if turn_time == 4:

#         nx, ny = x - dx[direction], y - dy[direction]

#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0

# print(count)

# 2회

n, m = map(int,input().split())

x, y, dir = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit = [(x,y)]

chk = True
while chk:

    for i in range(4):

        nextDir = (dir - (i+1)) % 4

        nextX, nextY = x + dx[nextDir], y + dy[nextDir]

        if board[nextX][nextY] == 0 and 0 <= nextX < n and 0 <= nextY < m and (nextX, nextY) not in visit:

            x = nextX
            y = nextY
            visit.append((x,y))
            dir = nextDir

            break

        if i == 3:
            if board[x - dx[dir]][y - dy[dir]] != 1:        
                x = x - dx[dir]
                y = y - dy[dir]
            else:
                chk = False


print(len(set(visit)))






