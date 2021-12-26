def solution(a, b):
    ans=0;
    date=['FRI','SAT','SUN','MON','TUE','WED','THU']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range (0,a-1):
        ans+=month[i]
    
    ans+=b-1;
    answer=date[ans%7]
    
    return answer
print(solution(5, 24))
