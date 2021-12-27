# LRU 알고리즘 : list[0] : 가장 오래 참조가 되지 않은 것(LRU), list[-1] : 가장 최근 참조된 것(MRU)으로 가장 오랫동안 참조되지 않은 캐시를 교체하는 기법이다.
# cache hit : 원하는 데이터가 캐시에 존재할 경우 해당 데이터를 반환 -> 실행시간 : 1
# cache miss: 참조하고자 하는 데이터가 캐시에 존재하지 않을 경우    -> 실행시간 : 5

def solution(cacheSize, cities):
    answer = 5    #처음엔 데이터가 캐시에 존재하지 않으므로 5부터 시작한다.
    
    #(예외처리) cache의 크기가 0인 경우, 모두 cache miss로 처리한다.(ex 입출력 예제 6번)
    if(cacheSize==0):
        return len(cities)*5
    
    cache=[cities.pop().lower()]
    #도시이름 배열의 길이만큼 반복
    for x in range(len(cities)+1):
        if not cities:
            return answer
        # cache hit
        i=cities[-1].lower()
        if i in cache:
            answer+=1
            cache.remove(i)
            cache.append(cities.pop().lower())
        #cache miss
        else:
            if(len(cache)==cacheSize):
                cache.pop(0)    # (=) del cache[0]
            cache.append(cities.pop().lower())
            answer+=5
            
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
