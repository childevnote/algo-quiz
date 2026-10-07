# 프로그래머스 42862 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 2026-10-07

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    # 1. 자급자족 학생 제외: lost와 reserve에 모두 있으면 스스로 해결
    need = sorted(lost_set - reserve_set)
    # 2. 대여 가능한 여벌만 남기기
    give = reserve_set - lost_set
    for l in need:
        # 3. 번호가 작은 학생부터 앞번호 이웃에게 우선 대여
        if l - 1 in give:
            give.remove(l - 1)
        # 4. 없으면 뒷번호 이웃에게 대여
        elif l + 1 in give:
            give.remove(l + 1)
        # 5. 빌리지 못하면 수업에서 제외
        else:
            n -= 1
    return n
