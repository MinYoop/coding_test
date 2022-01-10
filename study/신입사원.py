# https://www.acmicpc.net/problem/1946

from sys import stdin

for i in range(int(stdin.readline())):
    people = []

    for j in range(int(stdin.readline())):
        people.append(list(map(int, stdin.readline().split())))

    people.sort()
    tmp = people[0][1]
    cnt = 1

    for j in range(len(people)):
        if tmp > people[j][1]:
            cnt += 1
            tmp = people[j][1]

    print(cnt)


