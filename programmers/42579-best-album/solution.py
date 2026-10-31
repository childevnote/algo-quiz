# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 2026-10-31

from collections import defaultdict


def solution(genres, plays):
    # 1. 장르별 총 재생 횟수와 곡 목록(고유 번호, 재생 횟수)을 모은다
    total_by_genre = defaultdict(int)
    songs_by_genre = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        total_by_genre[genre] += play
        songs_by_genre[genre].append((play, i))

    answer = []
    # 2. 장르를 총 재생 횟수 내림차순으로 정렬한다
    for genre in sorted(total_by_genre, key=lambda g: -total_by_genre[g]):
        # 3. 장르 내 곡을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬해 상위 2곡을 수록한다
        songs = sorted(songs_by_genre[genre], key=lambda s: (-s[0], s[1]))
        answer.extend(i for _, i in songs[:2])
    return answer
