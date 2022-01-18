from collections import deque

n, m = map(int,input().split())

board = [[] for _ in range(n+1)]



for i in range(m):

    x, y = map(int,input().split())

    board[x].append(y)
    board[y].append(x)

def bfs(start):

    q = deque()
    q.append(start)
    visited = [start]
    cnt = [0 for i in range(n + 1)]
    
    while q:
        

        
        # print(visited)
        # print(cnt)
        # print(q)
        x = q.popleft()
        # print(x)
        # print("-------------")

        for i in board[x]:
            if i not in visited:
                visited.append(i)
                q.append(i)
                cnt[i] = cnt[x] + 1
    
            
    return sum(cnt)

results =[]

for i in range(1,n+1):

    
    results.append(bfs(i))

print(results.index(min(results))+1)




    
        
        









