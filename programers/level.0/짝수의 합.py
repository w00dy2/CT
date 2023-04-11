# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):

answer =0
if n%2 == 0:
    if n == 2 or 0:
        answer += n
    else:
        answer = (n+2)*n/4
else:
    if n == 1:
        answer==0
    else:
        answer = (n+1)(n-1)/4

return answer
