def solution(new_id):
    ans = ''
    an=['_', '-', '.']
    #1단계
    new_id=new_id.lower()
    
    for k in new_id:
        if k.isalpha() or k.isdigit() or k in ['_', '-', '.']:
            ans+=k
    #3단계
    while '..' in ans:
        ans=ans.replace('..','.')
            
    #4단계
    if(len(ans)>1):
        if(ans[0]=='.'):
            ans=ans[1:] 
    else: 
        '.'
    if(ans[-1]=='.'):
        ans=ans[:-1]
        
    #5단계
    if(ans==''):
        ans='a'
        
    #6단계
    if(len(ans)>=16):
        ans=ans[0:15]
        if(ans[-1]=='.'):
            ans=ans[0:-1]
    #7단계    
    while len(ans)<=2:    
        ans+=ans[-1]
                 
    return ans

print(solution("...!@BaT#*..y.abcdefghijklm"))
