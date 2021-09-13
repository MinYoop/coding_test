# https://www.acmicpc.net/problem/18310

# 시간 초과 그냥 정렬 후 가운데값이 최소거리다..

# n = int(input())

# lst = list(map(int,input().split()))
# distance = [0] * n

# for i in range(n):
#     for j in lst:
#         distance[i] += abs(lst[i]-j)

# resultLst = []
# for i in range(n):
#     resultLst.append([distance[i],lst[i]])

# resultLst.sort()

# print(resultLst[0][1])



n = int(input())

lst = list(map(int,input().split()))

print(sorted(lst)[(n-1)//2])