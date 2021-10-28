# from collections import deque

# n, m, k, x = map(int,input().split())

# v = [[] for _ in range(n+1)]

# for _ in range(m):
#     start, end = map(int, input().split())
#     v[start].append(end)

# q = deque([x])

# distances = [-1] * (n+1)
# distances[x] = 0

# while q:
#     data = q.popleft()
#     for i in v[data]:
#         if distances[i] == -1:
#             distances[i] = distances[data] + 1
#             q.append(i)

# check = False

# for i in range(1,len(distances)):
#     if distances[i] == k:
#         print(i)
#         check = True
# if check == False:
#     print(-1)


from collections import deque
# 2회차 풀이

n, m, k, x = map(int,input().split())

e = [[] for i in range(n+1)]
distance = [ 0 for i in range(n+1)]


for i in range(n):

    a, b = map(int, input().split())
    e[a].append(b)

result = []
def bfs(x,k):
    
    q = deque()
    visited = [x]
    q.append(x)
    
    while q:

        v = q.popleft()

        for i in e[v]:
            if i not in visited:
                visited.append(i)
                distance[i] = distance[v] + 1
                if distance[i] == k:
                    
                    result.append(i)
                q.append(i)
bfs(x,k)

if len(result) == 0:
    print(-1)
else:
    for i in sorted(result):
        print(i)

    


