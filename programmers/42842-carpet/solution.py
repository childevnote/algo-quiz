# 카펫
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 풀이 날짜: 2026-10-22 (자동 풀이)

def solution(brown, yellow):
    # 노란 영역은 안쪽 직사각형 (가로 w, 세로 h)이라고 두면
    # 전체 가로 = w+2, 세로 = h+2 가 된다 (테두리 갈색이 1줄씩 감쌈)
    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h == 0:
            w = yellow // h  # ① 노란 영역의 약수쌍 = 가능한 내부 가로/세로
            if (w + 2) * (h + 2) == brown + yellow:  # ② 전체 격자 수와 일치하는 쌍 채택
                return [w + 2, h + 2]
    return []
