def solution(a, b):
    num = 0
    if a > b:
        for i in range(b, a+1):
            num += i
    else:
        for i in range(a, b+1):
            num += i
    return num
