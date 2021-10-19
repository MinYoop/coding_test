
position = input()



x = int(position[1]) - 1
y = ord(position[0])-ord('a')

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

result = 0

for i in range(8):

    xPos = x + dx[i]
    yPos = y + dy[i]

    if 0 <= xPos < 8 and 0 <= yPos < 8:
        result += 1

print(result)

