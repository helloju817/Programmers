def solution(n, lost, reserve):
    #여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    lost1  = set(lost)-set(reserve)
    reserve1 = set(reserve)-set(lost)
    
    #여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
    for i in reserve1:
        if i-1 in lost1:
            lost1.remove(i-1)
        elif i+1 in lost1:
            lost1.remove(i+1)
    return n - len(lost1)

print(solution(5,[2,4], [1,3,5]))

