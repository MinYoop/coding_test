
# 내가 푼 것

N, M = map(int,input().split())

array = list(map(int,input().split()))
cnt = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):

        if array[i] != j:
            cnt += 1

print(cnt)

#답