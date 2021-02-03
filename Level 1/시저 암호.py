def solution(s, n):
    s_list = []

    for i in range(len(s)):
        if s[i] != ' ':
            asc = ord(s[i]) + n
            if 65 <= ord(s[i]) <= 90:    # A(65) ~ Z(90)
                if asc > 90:
                    asc -= 26
        
            else:   # a(97) ~ z(122)
                if asc > 122:
                    asc -= 26
                    
            s_list.append(chr(asc))
        else:   # 공백일 경우
            s_list.append(s[i])
            
    return ''.join(s_list)
