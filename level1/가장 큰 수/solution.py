def solution(numbers):
    answer = ''
    numbers=list(map(str, numbers))
    numbers.sort(key=lambda x : x*3 , reverse=True)
    answer=str(int(answer.join(numbers)))
    """
    str(int(answer.join(numbers)))에서 int는 [0,0,0]의 경우 정답이 0으로 출력되도록 만들기 위함.
    """
    
    return answer
#print(solution([6,0,2]))
#print(solution([0,0,0]))
