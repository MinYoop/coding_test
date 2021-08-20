
N, K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(K):

    A.sort()
    B.sort(reverse=True)

    if A[0] < B[0]:
        A[0], B[0] = B[0], A[0]

print(sum(A))
