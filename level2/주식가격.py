def solution(prices):
    answer = []
    
    for x in range(len(prices)-1):
        count=0
        for y in range(x+1, len(prices)):
            count+=1
            if(prices[x]>prices[y]): 
                break
        answer.append(count)
    answer.append(0)
            
    return answer

print(solution([1,2,3,2,3]))
