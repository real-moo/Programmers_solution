def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            snum = numbers[i] + numbers[j]
            if i != j:
                result.append(snum)
    return sorted(set(result))
