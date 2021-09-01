# 답안 풀이랑 좀 다름
s = input()
cnt = 0
tmp = s[0]
chk = True

for c in s:

    if c != tmp:
        if chk == True:
            cnt += 1
            chk = False
            tmp = c
        else:
            chk = True
            tmp = c
print(cnt) 

