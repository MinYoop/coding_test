n, m = map(int,input().split())

lst = [ list(map(int,input().split())) for _ in range(n)]

result = -1e9

for i in lst:
    
    result = max(min(i), result)

print(result)



