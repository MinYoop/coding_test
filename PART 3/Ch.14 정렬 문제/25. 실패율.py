# https://programmers.co.kr/learn/courses/30/lessons/42889

# def solution(N, stages):
    
       
#     answer = []
#     rate = []

#     def count(s):

#         cnt = 0

#         for i in stages:

#             if i >= s:
#                 cnt += 1

#         return cnt
    
#     for i in range(1,N+1):
        
#         if count(i) == 0:
#             rate.append(0)
#         else:
#             rate.append(stages.count(i)/count(i))

#     for i in sorted(enumerate(rate),key= lambda x: x[1],reverse=True):
#         answer.append(i[0]+1)
#     return answer


def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1,N+1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key = lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer




