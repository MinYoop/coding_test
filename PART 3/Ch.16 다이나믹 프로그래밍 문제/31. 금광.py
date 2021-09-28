
t = int(input())


def cal(board, j, i, n , prePosition):

    dx = [-1,0,1]

    value = 0

    for x in range(3):
        
        if 0 <= prePosition+dx[x] < n:

            value = max(value, board[prePosition+dx[x]][i])

    return value 
    
for _ in range(t):

    n, m = map(int,input().split())

    lst = list(map(int,input().split()))

    board = [lst[i * m : i * m + m ] for i in range(n)]

    dp = [[[0,0]]*m for i in range(n)] # 각 행에서 출발 했을 때 각 열에 도착 했을 때 최대 값.

    for i in range(n):
        dp[i][0] = [board[i][0],i]

    for i in range(1,m):

        for j in range(n):

            dp[j][i][0] = cal(board,j,i,n,dp[j][i-1][1]) + dp[j][i-1][0]

    result = 0
    for i in range(n):

        result = max(result,dp[i][m-1][0])

    for i in dp:
        print(i)

    print(result)




    

