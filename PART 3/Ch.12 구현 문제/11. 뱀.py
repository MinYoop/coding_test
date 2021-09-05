
n = int(input())

k = int(input())

board = [[0] * n for _ in range(n)]

for i in range(k):
    x, y = map(int,input().split())
    board[x-1][y-1] = 1

l = int(input())

direction = []

for i in range(l):
    second, dl = input().split()
    direction.append((int(second),dl))
    
snake = [[0,0]]

chk = True
sec = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

def inbody():
    for piece in snake:

        if snake.count(piece) > 1:
            return True
    return False

while chk:

    # 연장
    sec += 1
    
    snake.insert(0,[snake[0][0] + dx[dir],snake[0][1] + dy[dir]])
    
    # 벽이나 몸에 박았는지 확인
    if snake[0][0] < 0 or snake[0][0] > n - 1 or snake[0][1] < 0 or snake[0][1] > n - 1 or inbody():
        break

    item = snake.pop()

    # 사과 체크
    if board[snake[0][0]][snake[0][1]] == 1:
        board[snake[0][0]][snake[0][1]] == 0
        snake.append(item)
        

    # 방향 체크 및 바꾸기
    if len(direction) != 0:

        if sec == direction[0][0]:
            
            #print("방향전환")

            if direction[0][1] == 'D':
                dir += 1
                if dir == 4:
                    dir = 0
            else:
                dir -= 1
                if dir == -1:
                    dir = 3            

            direction.pop(0)

print(sec)
    


