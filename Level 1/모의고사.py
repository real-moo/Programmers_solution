def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if one[i%len(one)] == answers[i]:
            result[0] += 1
        if two[i%len(two)] == answers[i]:
            result[1] += 1
        if three[i%len(three)] == answers[i]:
            result[2] += 1
    
    for idx, s in enumerate(result):
        if s == max(result):
            answer.append(idx+1)
    return answer
