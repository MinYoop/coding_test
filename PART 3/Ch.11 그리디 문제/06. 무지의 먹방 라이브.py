# 내가 푼 답 , 프로그래머스 실행결과는 통과, 효율성 테스트 실패...

def solution(food_times, k):
    
    cnt = 0
    p = 0
    
    while True:
        
        if food_times[p] != 0:
            if cnt == k:
                break
            food_times[p] -= 1
            cnt += 1
            
        p += 1
        if p == len(food_times):
            p = 0
        
        if sum(food_times) == 0:
            return -1
    
    return p+1

    ## 다시 풀어야함.