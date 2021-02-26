def solution(n, lost, reserve):
    n_reserve = set(reserve) - set(lost)
    n_lost = set(lost) - set(reserve)
    
    for i in n_reserve:
        # 여벌의 체육복을 가진 학생의 앞 번호 학생이 체육복을 잃어버린 경우
        if i-1 in n_lost:
            n_lost.remove(i-1)
        # 여벌의 체육복을 가진 학생의 뒷 번호 학생이 체육복을 잃어버린 경우
        elif i+1 in n_lost:
            n_lost.remove(i+1)
            
    return n - len(n_lost)
