

def binary_search(array, target, start, end):

    while start <= end:

        x = (start+end)//2

        if array[x] == target:

            return x

        if target < array[x]:

            end = x - 1
        else :
            start = x + 1

    return None

n = int(input())

array = list(map(int,input().split()))

m = int(input())

targetLst = list(map(int,input().split()))

for i in targetLst:

    result = binary_search(array, i, 0, n - 1)

    if result != None:
        print("yes", end= " ")
    else:
        print("no", end = " ")

