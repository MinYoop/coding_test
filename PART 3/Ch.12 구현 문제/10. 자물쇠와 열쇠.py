# from copy import deepcopy
# def rotate(key):
#         rKey = [[0] * len(key) for _ in range(len(key))]

#         for i in range(len(key)):
#             for j in range(len(key)):

#                 rKey[j][len(key)-1-i] = key[i][j]

#         return rKey

# def check(new_lock):

#     lock_length = len(new_lock) // 3

#     for i in range(lock_length, lock_length * 2):
#         for j in range(lock_length, lock_length * 2):

#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)

#     new_lock = [[0]* (n*3) for _ in range(n * 3)]

#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]

#     for rotation in range(4):
#         key = rotate(key)

#         for x in range(n * 2):
#             for y in range( n * 2):

#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]

#                 if check(new_lock) == True:
#                     return True

#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
           
#     return False
    
       

# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


#2회차 풀이 97점 뜸;

def rotate(lst, m):
    result = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            result[j][m-1-i] = lst[i][j]   
    
    return result


def sumCal(board, n, m):

    sum = 0

    for i in range(n):
        for j in range(n):

            if board[m-1 + i][m-1 + j] != 1:
                return False
    
    return True


def solution(key, lock):

    n = len(lock)
    m = len(key)

    boardLen = n + m * 2 - 2
    
    board = [[0] * boardLen for _ in range(boardLen)]

    for i in range(n):
        for j in range(n):
            board[m+i-1][m+j-1] = lock[i][j]

    for _ in range(4):
        key = rotate(key,m)

        for i in range(boardLen-m):
            for j in range(boardLen-m):

                for x in range(m):
                    for y in range(m):

                        board[i+x][j+y] += key[x][y]


                if sumCal(board, n, m):
                    
                    return True              
                           

                for x in range(m):
                    for y in range(m):

                        board[i+x][j+y] -= key[x][y]
  
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


