

# def binary_search(array, target, start, end):

#     while start <= end:

#         x = (start+end)//2

#         if array[x] == target:

#             return x

#         if target < array[x]:

#             end = x - 1
#         else :
#             start = x + 1

#     return None

# n = int(input())

# array = list(map(int,input().split()))

# m = int(input())

# targetLst = list(map(int,input().split()))

# for i in targetLst:

#     result = binary_search(array, i, 0, n - 1)

#     if result != None:
#         print("yes", end= " ")
#     else:
#         print("no", end = " ")





# 두번째 풀이

n = int(input())

lst = list(map(int,input().split()))

m = int(input())

findLst = list(map(int,input().split()))

result = []

lst.sort()

def binaryFind(start, end, find):

    if start > end:
        return "no"

    mid = (start + end) // 2

    if lst[mid] == find:
        return "yes"

    elif lst[mid] < find:         
         return binaryFind(mid + 1, end, find)
    else:
        return binaryFind(start, mid - 1, find)


for i in range(m):
    result.append(binaryFind(0, len(lst) - 1, findLst[i]))

print(" ".join(result))






    