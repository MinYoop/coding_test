
# 내가 푼 것

# N, M = map(int,input().split())

# array = list(map(int,input().split()))
# cnt = 0
# for i in range(len(array)):
#     for j in range(i+1,len(array)):

#         if array[i] != j:
#             cnt += 1

# print(cnt)


# 2회차 풀이



# n, m = map(int,input().split())

# lst = list(map(int,input().split()))
# result = 0
# for i in range(n):

#     for j in range(i+1,n):
#         if lst[i] != lst[j]:
#             result +=1

# print(result)


# 답

n, m = map(int,input().split())
data = list(map(int, input().split()))

array = [0] * 11

for i in data:

    array[i] += 1

result = 0

for i in range(1, m + 1):
    
    n -= array[i]
    result += array[i] * n

print(result)