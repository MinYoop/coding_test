# n, k = map(int, input().split())

# cnt = 0

# while n != 1:

#     if n % k == 0:
#         n = n//k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1

# print(cnt)



# n이 k의 배수가 되도록 효율적으로 한번에 빼는 방식 소스코드

n, k = map(int, input().split())
result = 0

while True:
    # N == k로 나누어떨어지는 수 가 될 떄까지 1씩 빼기

    target = (n//k) * k

    result += (n - target)

    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)

