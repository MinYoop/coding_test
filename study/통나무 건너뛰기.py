n = int(input())

for i in range(n):
    m = int(input())
    lst = sorted(list(map(int,input().split())))
    result = 0

    for j in range(2,len(lst)):
        
        result = max(result, lst[j] - lst[j-2])
    print(result)

