
# n, m  = map(int,input().split())

# array = list(map(int,input().split()))


# def binary_search(array, m, start, end): 

#     result = 0
#     while start <= end:
            
#         mid = (start+end)//2

#         sum = 0
        

#         for x in array:
#             if x > mid:
#                 sum += x - mid
        
#         if sum >= m:
#             result = mid
#             start = mid + 1
#         else:
#             end = mid - 1

#     return result


# print(binary_search(array, m, 0, max(array)))


n, m = map(int,input().split())

dducks = list(map(int,input().split()))

def sumDduck(x):

    sum = 0

    for dduck in dducks:
        if x < dduck:
            sum += (dduck - x)
            
    return sum

result = 0

def binary(start, end, m):

    if start > end:
        return 

    global result
    mid = (start + end) // 2    

    if sumDduck(mid) < m:
        binary(start, mid-1, m)
    else:
        result = mid
        binary(mid + 1, end, m)

binary(0, max(dducks), m)
print(result)


    


