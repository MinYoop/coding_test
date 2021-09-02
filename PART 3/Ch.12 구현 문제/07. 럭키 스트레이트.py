n = input()

left = n[:len(n)//2]
right = n[(len(n)//2):]

if sum(list(map(int,left))) == sum(list(map(int,right))):
    print("LUCKY")
else:
    print("READY")