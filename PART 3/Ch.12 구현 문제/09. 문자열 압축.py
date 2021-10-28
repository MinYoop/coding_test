

# def solution(s):
#     answer = len(s)

#     for step in range(1,len(s)+1):
        
#         st = ""
#         prev = s[0:step]
#         count = 1

#         for j in range(step, len(s), step):

#             if prev == s[j:j+step]:
#                 count += 1
#             else:
#                 st += str(count) + prev if count > 1 else prev
#                 prev = s[j:j+step]
#                 count = 1
            
#         st += str(count) + prev if count > 1 else prev

#         answer = min(answer, len(st))
    
#     return(answer)


    # 2회독 풀이
def solution(s):

    answer = len(s)
    for i in range(1,len(s)//2+1):

        tmp = s[:i]
        cnt = 1
        stt = ""
        for j in range(i,len(s),i):

            if s[j:j+i] == tmp:
                cnt += 1
            else:
                if cnt > 1:
                    stt += (str(cnt) + tmp)
                else:
                    stt += tmp
                cnt = 1
                tmp = s[j:j+i]
        if cnt > 1:
            stt += (str(cnt) + tmp)
        else:
            stt += tmp
        # print(i, stt)
        answer = min(answer, len(stt))
        
    return answer

# print(solution("abababcdd"))