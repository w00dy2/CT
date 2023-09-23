# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer =''
    for i in my_string:
        if my_string[0:1] not in answer:
            answer += my_string[0:1]
            my_string = my_string[1:]
        else:
            my_string = my_string[1:]        
    return answer