from itertools import combinations

n, m = map(int,input().split())

board = []

for i in range(n):
    board.append(list(map(int,input().split())))

allChiken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            allChiken.append([i,j])

chikenArray = list(combinations(allChiken,m))

def cal_sum(combiArray): # 거리 구하기 함수
    
    sum = 0

    for i in range(n):
        for j in range(n):

            if board[i][j] == 1:
                tmp = 101
                for x, y in combiArray:
                    tmp = min(tmp,  abs(x-i) + abs(y-j))
                sum += tmp
    
    return sum

calLst = []

for combiArray in chikenArray:
    calLst.append(cal_sum(combiArray))

print(min(calLst))
