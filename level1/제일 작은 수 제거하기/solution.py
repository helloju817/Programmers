def solution(arr):
    answer = []
    arr.remove(min(arr))
    if(arr==[]):
        answer.append(-1)
    else:
        answer=arr
        
    return answer

print(solution([4,3,2,1]))
