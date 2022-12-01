def solution(arr, divisor):
    answer = []
    count = 0   #answer배열의 개수를 세어주는 변수
    
    for i in arr:
        if i%divisor == 0 :     #나누어 떨어질 경우
            answer.append(i)    #answer배열에 추가 
            count += 1          #count 증가
            
    if count == 0 :             #answer배열이 비어있다면
        answer.append(-1)       #answer배열에 -1 추가
        
    answer.sort()               #answer배열 오름차순으로 정렬
        
    return answer