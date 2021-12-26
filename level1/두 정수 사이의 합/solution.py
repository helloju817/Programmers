def solution(a, b):
    answer = 0
    if(a<b):
        for x in range(a,b+1):
            answer+=x
    elif(a>b):
        for x in range(b,a+1):
            answer+=x
    else:
        answer=a
    return answer

#print(solution(3,5))
