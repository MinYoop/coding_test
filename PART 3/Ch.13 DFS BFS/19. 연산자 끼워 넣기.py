
n = int(input())

aList = list(map(int,input().split()))

cal = list(map(int,input().split()))

maxValue = -1e9
minValue = 1e9
cnt = 0

def dfs(value, cnt):

    global maxValue
    global minValue
    global cal

    if cnt == n-1:
        maxValue = max(maxValue, value)
        minValue = min(minValue, value)
        
        return

    if cal[0] > 0:
        cal[0] -= 1
        dfs(value + aList[cnt+1], cnt + 1)
        cal[0] += 1

    if cal[1] > 0:
        cal[1] -= 1
        dfs(value - aList[cnt+1], cnt + 1)
        cal[1] += 1

    if cal[2] > 0:
        cal[2] -= 1
        dfs(value * aList[cnt+1], cnt + 1)
        cal[2] += 1
    
    if cal[3] > 0:
        cal[3] -= 1
        dfs(int(value / aList[cnt+1]), cnt + 1)
        cal[3] += 1

    

dfs(aList[0], cnt)

print(maxValue)
print(minValue)