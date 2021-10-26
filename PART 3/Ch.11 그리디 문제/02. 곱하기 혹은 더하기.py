# 내 풀이
# array = list(map(int,list(input())))

# result = 0

# for i in range(len(array)):

#     result = max(result+array[i],result*array[i])

# print(result)

# 답
# data = input()

# result = int(data[0])

# for i in range(1, len(data)):

#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)

    
# 2회독

# 2회독 풀이


n = input()

result = int(n[0])

for i in range(1, len(n)):

    num = int(n[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
