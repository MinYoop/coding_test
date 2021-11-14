# # 내가 푼 답 , 프로그래머스 실행결과는 통과, 효율성 테스트 실패...

# def solution(food_times, k):
    
#     cnt = 0
#     p = 0
    
#     while True:
        
#         if food_times[p] != 0:
#             if cnt == k:
#                 break
#             food_times[p] -= 1
#             cnt += 1
            
#         p += 1
#         if p == len(food_times):
#             p = 0
        
#         if sum(food_times) == 0:
#             return -1
    
#     return p+1

#     ## 다시 풀어야함.

# print(solution([3, 1, 2],5))
# 2회차 
# 


import heapq

def solution(food_times, k):

    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1 ))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times)

    while sum_value + (q[0][0] - previous) * length <= k: 
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    result = sorted(q, key = lambda x: x[1]) # 음식 번호 기준으로 정렬

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력

    return result[(k - sum_value) % length][1]

print(solution([3, 1, 2],5))
