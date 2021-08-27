
n, m  = map(int,input().split())

array = list(map(int,input().split()))


def binary_search(array, m, start, end): 

    result = 0
    while start <= end:
            
        mid = (start+end)//2

        sum = 0
        

        for x in array:
            if x > mid:
                sum += x - mid
        
        if sum >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


print(binary_search(array, m, 0, max(array)))