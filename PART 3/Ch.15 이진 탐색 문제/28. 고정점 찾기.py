
# n = int(input())
# lst = list(map(int,input().split()))


# def binary(start, end):
    
#     if start > end:
#         return -1
#     mid = (start + end) // 2

#     if mid == lst[mid]:
#         return mid
#     elif mid < lst[mid]:
#         return binary(start, mid-1)
#     else:
#         return binary(mid+1, end)

# print(binary(0,n-1))



n = int(input())

lst = list(map(int,input().split()))

def binary(lst, start, end):


    if start > end:
        return -1
    mid = (start + end)//2


    if lst[mid] == mid:

        return mid

    elif lst[mid] < mid:

        return binary(lst, mid + 1, end)
    
    else:
        return binary(lst, start, mid -1)

print(binary(lst,0,len(lst)-1))


    


