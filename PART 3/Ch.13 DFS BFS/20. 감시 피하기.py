# from itertools import combinations

# n = int(input())

# board = []
# teachers = []
# spaces = []

# for i in range(n):
#     board.append(list(input().split()))
#     for j in range(n):

#         if board[i][j] == 'T':
#             teachers.append((i,j))

#         if board[i][j] == 'X':
#             spaces.append((i,j))

# def watch(x,y,direction):

#     if direction == 0:
#         while y >= 0:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == '0':
#                 return False
#             y -= 1
    
#     if direction == 1:
#         while y < n:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == '0':
#                 return False
#             y += 1

#     if direction == 2:
#         while x >= 0:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == '0':
#                 return False
#             x -= 1
#     if direction == 3:
#         while x < n:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == '0':
#                 return False
#             x += 1

#     return False

# def process():

#     for x,y in teachers:

#         for i in range(4):
#             if watch(x, y, i):
#                 return True
        
#     return False

# find = False

# for data in combinations(spaces, 3):

#     for x,y in data:
#         board[x][y] = '0'

#     if not process():

#         find = True
#         break

#     for x,y in data:
#         board[x][y] = 'X'

# if find:
#     print('YES')
# else:
#     print('NO')


    



# 2회차 풀이


n = int(input())

board = [input().split() for _ in range(n)]

def check(board): # 찾을 수 있는지 체크

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # for i in board:
    #     print(i)
    # print("-----------------")
    for i in range(n):
        for j in range(n):

            if board[i][j] == 'T':

                for k in range(4):

                    x, y = i, j

                    while board[x][y] != 'O':

                        x += dx[k]
                        y += dy[k]

                        if x < 0 or x >= n or y < 0 or y >= n:
                            break

                        if board[x][y] == 'S':
                            return False

    return True

flag = False

def dfs(cnt):
    global flag
    global board

    if flag == True:
        return

    if cnt == 3:
        if check(board):
            # for i in board:
            #     print(i)
            flag = True
        
        return

    for i in range(n):
        for j in range(n):

            if board[i][j] == 'X':

                board[i][j] = 'O'
                dfs(cnt+1)
                board[i][j] = 'X'

dfs(0)

if flag:
    print("YES")
else:
    print("NO")