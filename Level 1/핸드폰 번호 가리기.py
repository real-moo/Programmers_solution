def solution(phone_number):
    result = []
    for i in range(len(phone_number)):
        if i < (len(phone_number)-4):
                   result.append('*')
        else:
                   result.append(phone_number[i])
    return ''.join(result)
