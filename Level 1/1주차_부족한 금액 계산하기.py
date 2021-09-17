def solution(price, money, count):
    answer = []
    
    for i in range(1, count+1):
        answer.append(price * i)
    
    result = sum(answer) - money
    
    if (result <= 0) :
        return 0
    else:
        return result
