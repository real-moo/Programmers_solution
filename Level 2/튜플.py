def solution(s):
    result_arr = []
    s = s[2:-2]
    s_arr = s.split('},{')
    s_arr.sort(key = len)
    
    for i in s_arr:
        new_arr = i.split(',')
        for j in new_arr:
            if int(j) not in result_arr:
                result_arr.append(int(j))
                
    return result_arr
