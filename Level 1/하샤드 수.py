def solution(x):
    snum = sum(list(map(int, str(x))))   # 자릿수의 합
    if x % snum == 0:
        return True
    else:
        return False
