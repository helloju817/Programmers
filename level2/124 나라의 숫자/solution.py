def solution(n):
    a=[1,2,4]
    answer = ''
    while(n>0):
        n=n-1
        answer = str(a[n%3])+answer
        n=n//3
    return answer

#print(solution(5))
