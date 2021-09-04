

def solution(s):
    answer = len(s)

    for step in range(1,len(s)+1):
        
        st = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):

            if prev == s[j:j+step]:
                count += 1
            else:
                st += str(count) + prev if count > 1 else prev
                prev = s[j:j+step]
                count = 1
            
        st += str(count) + prev if count > 1 else prev

        answer = min(answer, len(st))
    
    return(answer)