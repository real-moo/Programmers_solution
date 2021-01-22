def solution(a, b):
    rlist = []
    for i in range(len(a)):
        result = a[i] * b[i]
        rlist.append(result)
    return sum(rlist)
