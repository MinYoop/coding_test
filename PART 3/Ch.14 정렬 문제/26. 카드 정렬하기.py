# # https://www.acmicpc.net/problem/1715
# # 내 풀이 시간초과
# # n = int(input())

# # lst = [ int(input()) for i in range(n)]
# # result = 0
# # for i in range(n-1):

# #     lst.sort()

# #     x = lst[0] + lst[1]

# #     result += x

# #     lst = [x] + (lst[2:] if len(lst) > 2 else [])

# # print(result)

# import heapq

# n = int(input())

# heap = []

# for i in range(n):

#     data = int(input())
#     heapq.heappush(heap,data)

# result = 0

# while len(heap) != 1:

#     one = heapq.heappop(heap)
#     two = heapq.heappop(heap)

#     sum_value = one + two
#     result += sum_value
#     heapq.heappush(heap, sum_value)

# print(result)




# 2회차 풀이
from collections import deque

n = int(input())

lst = [int(input()) for _ in range(n)]

lst.sort()
sum = 0
cnt = 0

for i in range(len(lst)-1):


    cnt = lst[0]
    cnt += lst[1]
    lst.remove(lst[0])
    lst.remove(lst[0])

    sum += cnt
    lst.append(cnt)
    lst.sort()

print(sum)

    