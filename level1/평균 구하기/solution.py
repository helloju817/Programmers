def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer+=arr[i]
    
    return answer/len(arr)

print(solution([5,5]))
