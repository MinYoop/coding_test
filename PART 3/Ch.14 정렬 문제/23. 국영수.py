# https://www.acmicpc.net/problem/10825

n = int(input())


lst = []
for i in range(n):
    lst.append(input().split())

lst.sort(key= lambda x: (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))

for i in lst:
    print(i[0])

