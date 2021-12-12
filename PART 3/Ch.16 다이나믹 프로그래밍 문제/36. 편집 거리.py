
# a = input()
# b = input()

# dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

# for i in range(len(b)+1):

#     dp[0][i] = i

# for i in range(len(a)+1):

#     dp[i][0] = i

# for i in range(1,len(a)+1):
#     for j in range(1,len(b)+1):

#         if b[j-1] == a[i-1]:

#             dp[i][j] = dp[i-1][j-1]

#         else:
#             dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

# print(dp[len(a)][len(b)])

for i in dp:
    print(i)


def edit_dist(str1, str2):

    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1 for _ in range(n+1))]

    for i in range(1, n+1):
        dp[i][0] = i

    for j in range(1, m+1):
        dp[0][j] = j
    
    for i in range(1, n+1):
        for j in range(1, m+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))
