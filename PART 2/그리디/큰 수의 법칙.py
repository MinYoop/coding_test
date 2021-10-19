# n, m, k = map(int,input().split())
# lst = list(map(int,input().split()))


# lst.sort(reverse = True)
# one = lst[0]
# two = lst[1]

# cnt = 0

# chk = True
# sum = 0
# while cnt < m:

#     if chk:
#         for _ in range(k):

#             sum += one
#             cnt += 1
#             if cnt == m:
#                 break
#         chk = False
#     else:
        
#         sum += two
#         cnt += 1
#         if cnt == m:
#             break
#         chk = True

# print(sum)


# 효율적 풀이        

n, m, k = map(int,input().split())
lst = list(map(int,input().split()))


lst.sort(reverse = True)
one = lst[0]
two = lst[1]    

sum = one * k + two

result = sum * (m // (k+1)) + (one * m % (k+1))

print(result)


