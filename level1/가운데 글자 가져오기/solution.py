def solution(s):
    answer = ''
    i=len(s)//2
    if(len(s)%2!=0):
        answer+=s[i]
    else:
        answer+=s[i-1]
        answer+=s[i]
    print(answer)
    return answer


solution("abcde")
solution("qwer")
