# https://www.acmicpc.net/problem/1920

n = int(input())

board = list(map(int,input().split()))

m = int(input())

findNumbers = list(map(int,input().split()))

board.sort()

def binary(start, end, findNumber):

    if start > end:
        return 0   

    mid = (start + end)//2

    if board[mid] == findNumber:
        return 1    
    
    if findNumber > board[mid]:
        return binary(mid + 1, end, findNumber)
    else:
        return binary(start, mid - 1, findNumber)

end = len(board) - 1
for i in range(m):

    print(binary(0,end ,findNumbers[i]))





        

