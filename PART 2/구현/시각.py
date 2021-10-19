

n = int(input())


cnt = 0

for h in range(n+1):

    for m in range(60):

        for j in range(60):
            
            if '3' in str(h) + str(m) + str(j):
                
                cnt += 1

print(cnt)
