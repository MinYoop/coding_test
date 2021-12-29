# from collections import deque

# n = int(input())

# board = [list(map(int,input().split())) for _ in range(n)]

# shark = 2
# eated = 0 
# sharkLoc = None

# time = 0

# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 9:
#             sharkLoc = [i,j,0]
#             board[i][j] = 0
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# def bfs(board):
#     global shark
#     global sharkLoc
#     global eated
#     visited = []

#     q = deque()
#     minLoc = 1e9
#     q.append(sharkLoc)
#     tmp = 0
#     while q:

#         locX, locY, time = q.popleft()
#         visited.append([locX,locY])
        

#         if board[locX][locY] < shark and board[locX][locY] != 0:
#             eated += 1
#             if eated == shark:
#                 eated = 0
#                 shark += 1

#             board[locX][locY] = 0
#             sharkLoc = [locX,locY,time]
            
#             return time

#         for i in range(4):
#             x, y = locX + dx[i], locY + dy[i]

#             if 0 <= x < n and 0 <= y < n  and board[x][y] <= shark:
#                 if [x,y] not in visited:
#                     q.append([x,y,time+1])
#     return 0




# nothing = False

# while not nothing:

#     # print(shark,board)
#     # print(sharkLoc)
#     # print("-----------")
    
    
#     tmpTime = bfs(board)
    
#     if tmpTime == 0:
#         nothing = True
        

# print(sharkLoc[2])

# 테스트케이스만 통과, 시간초과 뜸, 아래 정답

from collections import deque
INF = 1e9 # 무한을 의미하는 값으로 10억을 설정

# 맵의 크기 N을 입력받기

n = int(input())

# 전체 모든 칸에 대한 정보 입력

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0,0

# 아기 상어의 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최소 거리만' 계산하는 bfs 함수

def bfs():

    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]

    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # w자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    # 모든 위치까지의 최단 거리 테이블 반환
    return dist

#최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):

            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:

                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF: #먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x,y, min_dist # 먹을 물고기의 위치와 최단 거리

    
result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]

        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate+= 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0
