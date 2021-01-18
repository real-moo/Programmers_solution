def solution(s):
    num = len(s) // 2
    if len(s)%2 == 0:   # 짝수
        return s[num-1]+s[num]
    else:               # 홀수
        return s[num]
