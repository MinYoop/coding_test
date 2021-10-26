# # 답안 풀이랑 좀 다름
# s = input()
# cnt = 0
# tmp = s[0]
# chk = True

# for c in s:

#     if c != tmp:
#         if chk == True:
#             cnt += 1
#             chk = False
#             tmp = c
#         else:
#             chk = True
#             tmp = c
# print(cnt) 

# 2회독 풀이


n = list(map(int,list(input())))

prev = n[0]
start = prev

cnt = 0
for i in range(1,len(n)):

    if n[i] != prev:
        prev = n[i]
        if start != n[i]:
            cnt += 1
        

print(cnt)









