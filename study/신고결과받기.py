# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):

    answer = [0 for i in range(len(id_list))]
    declaredUsers = dict()

    for i in range(len(id_list)):

        declaredUsers[id_list[i]] = set()

    for i in range(len(report)):
        
        a, b = report[i].split()

        declaredUsers[b].add(a)

    for key in list(declaredUsers.keys()):

        if len(declaredUsers[key]) >= k:

            for user in declaredUsers[key]:
                answer[id_list.index(user)] += 1


    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)