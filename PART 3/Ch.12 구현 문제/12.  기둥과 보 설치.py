# def possible(answer):
    
#     for x, y, a in answer:

#         if a == 0: # 기둥 : 바닥 위 / 보 양쪽 끝 / 기둥 위
#             if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
#                 continue
#             return False

#         else: # 보 : 기둥 위 / 양쪽 끝이 보랑 연결

#             if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
#                 continue
#             return False
    
#     return True


# def solution(n, build_frame):
#     answer = []

#     for frame in build_frame:
#         x, y, a, b = frame

#         if b == 1:
#             answer.append([x,y,a])
#             if not possible(answer):
#                 answer.remove([x,y,a])
#         else:
#             answer.remove([x,y,a])
#             if not possible(answer):
#                 answer.append([x,y,a])
#     return sorted(answer) 

# 2회차 풀이

def solution(n, build_frame):
    answer = []

    def chk1(x,y,a):

        if a == 0:

            if (y == 0 or (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer ):
                return True

            else:
                return False
        else:

            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):

                return True
            else:
                return False

    def chk2(x,y,a):

        answer.remove((x,y,a))

        for i, j, k in answer:

            if not chk1(i,j,k):
                answer.append((x,y,a))
                return False
        answer.append((x,y,a))
        return True



        

    for x, y, a, b in build_frame:

        
        if b == 1:
            
            if chk1(x,y,a):

                answer.append((x,y,a))
            else:
                continue

        else:
            
            if chk2(x,y,a):

                answer.remove((x,y,a))
            else:
                continue

    answer = list(map(list,answer))

    answer.sort(key = lambda x : (x[0],x[1],x[2]))

    return answer



print(solution(5,	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))