def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i]<=budget:
            answer+=1
            budget-=d[i]
        
        
    return answer
#print(solution([2,2,3,3],10))
