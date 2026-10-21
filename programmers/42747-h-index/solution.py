# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 날짜: 2026-10-20
def solution(citations):
    citations = sorted(citations, reverse=True)
    h = 0
    for i, c in enumerate(citations, start=1):
        if c >= i:
            h = i
        else:
            break
    return h

if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))  # expected 3
    print(solution([10, 8, 5, 4, 3]))  # expected 4
    print(solution([0, 0, 0]))  # expected 0
    print(solution([100]))  # expected 1
    print(solution([6, 6, 6, 6, 6]))  # expected 5
    print(solution([4, 4, 4]))  # expected 3
