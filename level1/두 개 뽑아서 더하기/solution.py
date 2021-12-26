#방법 1
def solution(numbers):
    answer = []
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if(x!=x-y):
                answer.append(numbers[x]+numbers[x-y])
    answer=sorted(set(answer))
                
    return answer
"""
#방법 2
def solution(numbers):
    answer = []
    for x in range(len(numbers)):
        for y in range(x+1, len(numbers)):
            answer.append(numbers[x]+numbers[y])
    answer=sorted(set(answer))
                
    return answer
"""

#print(solution([2,1,3,4,1]))
