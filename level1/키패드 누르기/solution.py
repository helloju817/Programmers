def solution(numbers, hand):
    answer = ''
    L=10
    R=12
    for k in numbers:
        if k in [1,4,7]:
            answer += "L"
            L=k
        elif k in [3,6,9]:
            answer+="R"
            R=k
        
        else:
            if k==0:
                k=11
            else: 
                k
            #k=11 if k==0 else k
            
            if(sum(divmod(abs(k-L),3))>sum(divmod(abs(k-R),3))):
                answer+="R"
                R=k
            elif(sum(divmod(abs(k-L),3))<sum(divmod(abs(k-R),3))):
                answer+="L"
                L=k
            else:
                if(hand=="right"):
                    answer+="R"
                    R=k
                if(hand=="left"):
                    answer+="L"
                    L=k
              
    return answer
#print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
