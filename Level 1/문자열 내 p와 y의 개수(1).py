def solution(s):
    s_list = sorted(list(map(str, s.lower())))
    p_count = 0
    y_count = 0
    
    for i in range(len(s_list)):
        if s_list[i] == 'p':
            p_count += 1
        elif s_list[i] == 'y':
            y_count += 1
            
    if p_count == y_count:
        return True
    else:
        return False
