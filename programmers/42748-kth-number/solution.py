# 프로그래머스 42748 K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 2026-10-03

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # 1. 1-based 구간 [i, j]를 0-based 슬라이스로 자르기
        sliced = array[i-1:j]
        # 2. 복사본을 정렬 (원본 훼손 없음)
        sliced = sorted(sliced)
        # 3. k번째 수 (1-based → 0-based)
        answer.append(sliced[k-1])
    return answer
