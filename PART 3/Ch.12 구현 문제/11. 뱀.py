
# n = int(input())

# k = int(input())

# board = [[0] * n for _ in range(n)]

# for i in range(k):
#     x, y = map(int,input().split())
#     board[x-1][y-1] = 1

# l = int(input())

# direction = []

# for i in range(l):
#     second, dl = input().split()
#     direction.append((int(second),dl))
    
# snake = [[0,0]]

# chk = True
# sec = 0

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# dir = 0

# def inbody():
#     for piece in snake:

#         if snake.count(piece) > 1:
#             return True
#     return False

# while chk:

#     # 연장
#     sec += 1
    
#     snake.insert(0,[snake[0][0] + dx[dir],snake[0][1] + dy[dir]])
    
#     # 벽이나 몸에 박았는지 확인
#     if snake[0][0] < 0 or snake[0][0] > n - 1 or snake[0][1] < 0 or snake[0][1] > n - 1 or inbody():
#         break

#     item = snake.pop()

#     # 사과 체크
#     if board[snake[0][0]][snake[0][1]] == 1:
#         board[snake[0][0]][snake[0][1]] == 0
#         snake.append(item)
        

#     # 방향 체크 및 바꾸기
#     if len(direction) != 0:

#         if sec == direction[0][0]:
            
#             #print("방향전환")

#             if direction[0][1] == 'D':
#                 dir += 1
#                 if dir == 4:
#                     dir = 0
#             else:
#                 dir -= 1
#                 if dir == -1:
#                     dir = 3            

#             direction.pop(0)

# print(sec)
    
from collections import deque

n = int(input())
k = int(input())

lst = list()
changes = list()
snake = deque()

for i in range(k):
    x, y = map(int,input().split())
    lst.append((x,y))

l = int(input())

for i in range(l):
    x, c = input().split()
    changes.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake.append((1,1)) # 오른쪽이 머리
direction = 0
time = 0
while True:
    print(snake)
    time += 1
    cnt = None

    x = snake[-1][0] + dx[direction]
    y = snake[-1][1] + dy[direction]

    # 자기랑 부딪히는지 확인

    if (x,y) in snake:
        break

    # 벽 확인

    if 1 <= x <= n and 1 <= y <= n: 

        snake.append((x,y))
        cnt = snake.popleft()

    else:
        break

    # 사과 확인

    if (x,y) in lst:
        snake.appendleft(cnt)
        lst.remove((x,y))

    # 변화 확인

    for change in changes:
        if change[0] == time:

            if change[1] == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3
            else:
                direction += 1
                if direction == 4:
                    direction = 0

print(time)

    


    