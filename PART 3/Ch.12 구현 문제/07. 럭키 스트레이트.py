# 2회독 풀이

s = input()
left, right = sum(map(int,s[:len(s)//2])), sum(map(int,s[len(s)//2:]))

if left == right:
    print("LUCKY")
else:
    print("READY")


