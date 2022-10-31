def solution(phone_number):
    answer = ''
    secret_number = phone_number[-4:]
    for i in range(len(phone_number)-4):
        answer += "*"
    
    answer += secret_number
    return answer