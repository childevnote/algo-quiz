# https://school.programmers.co.kr/learn/courses/30/lessons/12925
# 2026-11-22

def solution(s):
    # 1. 맨앞 부호를 확인한다. '-'이면 음수, '+'이거나 없으면 양수이다.
    # 2. 숫자 자릿수를 왼쪽부터 한 자리씩 누적한다: result = result * 10 + digit.
    #    '0' 문자의 코드값을 빼면 문자 '3'은 숫자 3이 된다.
    # 3. 음수이면 부호를 뒤집어 반환한다.
    negative = s[0] == '-'
    start = 1 if s[0] in '+-' else 0
    result = 0
    for i in range(start, len(s)):
        result = result * 10 + (ord(s[i]) - ord('0'))
    return -result if negative else result
