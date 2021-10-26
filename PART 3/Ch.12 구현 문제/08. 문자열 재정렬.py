
# s = input()

# alpha = []

# for i in range(65,91):
#     alpha.append(chr(i))

# sum = 0

# chrLst = []

# for i in range(len(s)):

#     if s[i] in alpha:
#         chrLst.append(s[i])
#     else:
#         sum += int(s[i])

# print("".join(sorted(chrLst)) + str(sum))


# 2회독 풀이


n = input()

alpha = []
num = []

for i in n:

    if i.isalpha():
        alpha.append(i)
    else:
        num.append(i)

# print(alpha)
# print(num)
print("".join(sorted(alpha)) + str(sum(map(int,num))))

