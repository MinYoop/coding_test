
s = input()

alpha = []

for i in range(65,91):
    alpha.append(chr(i))

sum = 0

chrLst = []

for i in range(len(s)):

    if s[i] in alpha:
        chrLst.append(s[i])
    else:
        sum += int(s[i])

print("".join(sorted(chrLst)) + str(sum))
