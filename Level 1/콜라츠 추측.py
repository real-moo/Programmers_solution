def solution(num):
    count = 0
    
    while True:
        # num이 1이 되면 작업 횟수 반환
        if num == 1:
            return count
        count += 1
        # num이 짝수일 경우, num / 2
        if num % 2 == 0:
            num /= 2
        # num이 홀수일 경우, num * 3 + 1
        else:
            num = num * 3 + 1
        # 작업을 500번 반복해도 1이 되지 않는다면 -1 반환
        if count == 500:
            return -1
