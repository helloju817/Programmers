def solution(citations):
    citations.sort()
    count=len(citations)    #5
    for x in range(count):
        #[0,1,3,5,6]
        if(citations[x] >= count-x):
            return count-x
    return 0

print(solution([3,0,6,1,5]))
