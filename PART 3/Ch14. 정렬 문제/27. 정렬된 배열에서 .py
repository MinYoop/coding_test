

# n, x = map(int,input().split()) 
# lst = list(map(int,input().split()))

# start = 0
# end = n-1

# k = 0
# finded = False
# while start < end:

#     if lst[(start+end)//2] == x:
#         k = (start+end)//2
#         finded = True
#         break
    
#     if (start+end)//2 < x:
#         start = (start+end)//2 + 1
#     else:
#         end = (start+end)//2 - 1

# if finded :

#     chk = True
#     cnt = 1

#     left = k

#     while chk:
#         left -= 1
#         if lst[left] == x:
#             cnt += 1
#         else:
#             chk = False

#     right = k

#     chk = True

#     while chk:
#         right += 1
#         if lst[right] == x:
#             cnt += 1
#         else:
#             chk = False

#     print(cnt)

# else:
#     print(-1)

# bisect 라이브러리 활용

from bisect import bisect_left, bisect_right

n, x = map(int,input().split())

lst = list(map(int,input().split()))


def countTarget(lst, x):

    firstIndex = bisect_left(lst,x)
    lastIndex = bisect_right(lst,x)

    return lastIndex - firstIndex

cnt = countTarget(lst,x)

if cnt == 0:
    print(-1)
else:
    print(cnt)



