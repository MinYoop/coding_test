from collections import deque

n, m, k, x = map(int,input().split())

v = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    v[start].append(end)

q = deque([x])

distances = [-1] * (n+1)
distances[x] = 0

while q:
    data = q.popleft()
    for i in v[data]:
        if distances[i] == -1:
            distances[i] = distances[data] + 1
            q.append(i)

check = False

for i in range(1,len(distances)):
    if distances[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)



