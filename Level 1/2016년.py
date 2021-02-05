def solution(a, b):
    # 1월 1일이 금요일이기 때문에 week[0] = FRI로 시작
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 각 달의 day 개수
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    
    # 해당 월의 바로 전월까지만의 day를 더함
    for i in range(a-1):
        sum += month[i]
    # sum에 b를 더해주고 1을 빼줌(배열은 0부터 시작이기 때문)
    sum += b -1
    
    return week[sum%7]
