def possible(answer):
    
    for x, y, a in answer:

        if a == 0: # 기둥 : 바닥 위 / 보 양쪽 끝 / 기둥 위
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False

        else: # 보 : 기둥 위 / 양쪽 끝이 보랑 연결

            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame

        if b == 1:
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])
        else:
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
    return sorted(answer) 

# 2회차 풀이

def solution(n, build_frame):
    answer = []

    return answer