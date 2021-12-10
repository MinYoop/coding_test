# d[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이 
# 가장 긴 증가하는 부분 수열

# n = int(input())

# array = list(map(int, input().split()))
# array.reverse()

# dp = [1] * n

# for i in range(1,n):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(n - max(dp))

n = int(input())

array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))














