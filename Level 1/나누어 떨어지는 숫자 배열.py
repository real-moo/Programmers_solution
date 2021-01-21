def solution(arr, divisor):
    result = []
    # 나누어 떨어지는 값
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            dnum = arr[i]
            result.append(dnum)
    # 빈 배열일 경우 -1        
    if not result:
        result.append(-1)
                
    return sorted(result)
