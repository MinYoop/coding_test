
n = int(input())

directionList = list(input().split())

x, y = 1, 1

for dir in directionList:

    if dir == 'L':
        if y > 1:
            y -= 1
    elif dir == 'R':
        if y < n:
            y += 1
    elif dir == 'U':
        if x > 1:
            x -= 1
    else:
        if x < n:
            x += 1

print(x, y)


