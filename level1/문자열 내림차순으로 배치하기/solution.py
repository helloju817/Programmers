def solution(s):
    answer = ''
    answer=answer.join(sorted(s,reverse=True))
    return answer

print(solution("Zbcdefg"))
