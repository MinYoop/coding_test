N = int(input())


lst = list()
for i in range(N):
    lst.append(int(input()))


print(" ".join(list(map(str,sorted(lst, reverse=True)))))


