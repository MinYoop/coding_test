

# # n, x = map(int,input().split()) 
# # lst = list(map(int,input().split()))

# # start = 0
# # end = n-1

# # k = 0
# # finded = False
# # while start < end:

# #     if lst[(start+end)//2] == x:
# #         k = (start+end)//2
# #         finded = True
# #         break
    
# #     if (start+end)//2 < x:
# #         start = (start+end)//2 + 1
# #     else:
# #         end = (start+end)//2 - 1

# # if finded :

# #     chk = True
# #     cnt = 1

# #     left = k

# #     while chk:
# #         left -= 1
# #         if lst[left] == x:
# #             cnt += 1
# #         else:
# #             chk = False

# #     right = k

# #     chk = True

# #     while chk:
# #         right += 1
# #         if lst[right] == x:
# #             cnt += 1
# #         else:
# #             chk = False

# #     print(cnt)

# # else:
# #     print(-1)

# # bisect 라이브러리 활용

# from bisect import bisect_left, bisect_right

# n, x = map(int,input().split())

# lst = list(map(int,input().split()))


# def countTarget(lst, x):

#     firstIndex = bisect_left(lst,x)
#     lastIndex = bisect_right(lst,x)

#     return lastIndex - firstIndex

# cnt = countTarget(lst,x)

# if cnt == 0:
#     print(-1)
# else:
#     print(cnt)


n, x =  map(int,input().split())

lst = list(map(int,input().split()))

def left_binary(lst, start, end, x):
    global left

    if start > end:
        return -1
    mid = (end + start) // 2

    print("mid :",  mid)
    
    if lst[mid] == x and (mid == 0 or lst[mid - 1] < x):
        
        return mid

    if lst[mid] >= x:
        return left_binary(lst, start, mid - 1, x)
    else:
        return left_binary(lst, mid + 1, end, x)

def right_binary(lst, start, end, x):
    global right

    if start > end:
        return -1
    mid = (end + start) // 2
    
    if lst[mid] == x and (mid == n-1 or lst[mid + 1] > x):
        
        return mid

    if lst[mid] <= x:
        return right_binary(lst, mid + 1, end, x)
    else:
        return right_binary(lst, start, mid - 1, x)


right = right_binary(lst, 0 ,len(lst)-1,x)
left = left_binary(lst, 0 ,len(lst)-1,x)

if left == -1:
    print(-1)
else:
    print(right - left + 1)



