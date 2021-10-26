# # 틀림

# n = int(input())

# array = list(map(int,input().split()))


# array.sort()

# cnt = 0
# result = 0

# for i in array:

#     cnt += 1
#     if cnt >= i:
#         result += 1
#         cnt = 0

# print(result)

# 2회 풀이






n = int(input())

lst = list(map(int,input().split()))

lst.sort()

cnt = 0
result = 0
for i in lst:
    cnt += 1

    if i <= cnt:
        result += 1
        cnt = 0 

print(result)
























