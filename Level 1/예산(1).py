def solution(d, budget):
    new_d = sorted(d)   # 오름차순 정렬
    count = 0
    
    for i in range(len(d)):
        budget -= new_d[i]
        if budget < 0:
            return count
        count += 1
        
    return count
