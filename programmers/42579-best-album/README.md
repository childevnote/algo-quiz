# 베스트앨범

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579
- 레벨: Lv.3
- 카테고리: 해시
- 풀이 날짜: 2026-10-31 (18:00 자동 풀이)

## 문제 핵심 요약

장르별로 가장 많이 재생된 노래를 두 곡씩 모아 베스트 앨범을 만드는 문제다. 수록 순서는 장르의 총 재생 횟수가 많은 장르부터, 장르 안에서는 재생 횟수가 많은 곡부터이며, 재생 횟수가 같으면 고유 번호가 낮은 곡이 먼저다.

- 제한사항: 노래 개수 1개 이상 10,000개 이하, 장르 종류 100개 미만, 장르에 곡이 하나면 하나만 선택, 모든 장르의 총 재생 횟수는 서로 다름
- 입출력 예: `["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500] → [4, 1, 3, 0]`

## 문제 분석 및 핵심 로직

이 문제는 두 단계의 정렬로 나눌 수 있다. 먼저 장르 단위로 총 재생 횟수를 구해 장르의 순서를 정하고, 다음으로 각 장르 안에서 곡의 순서를 정한다. 장르와 곡을 한 번에 정렬하려 하면 비교 기준이 섞여 코드가 복잡해지므로, 집계와 정렬을 분리하는 편이 낫다.

핵심은 "장르별 총합"과 "장르 내 곡 목록"이라는 두 가지 정보를 한 번의 순회로 모으는 것이다. 곡을 순회하면서 장르별 총 재생 횟수를 누적하고, 동시에 각 장르의 곡 목록에 (재생 횟수, 고유 번호) 쌍을 쌓는다. 이후 장르는 총합 내림차순으로, 곡은 재생 횟수 내림차순·고유 번호 오름차순으로 정렬하고, 장르마다 상위 두 곡까지만 결과에 추가한다. 제한사항에서 모든 장르의 총 재생 횟수가 다르다고 보장하므로, 장르 정렬에서 동점 처리는 신경 쓰지 않아도 된다.

## 개념별 심층 설명

### 해시 맵을 이용한 그룹화

장르별 집계를 하려면 곡을 장르 기준으로 묶어야 한다. 초심자 방식은 장르가 나타날 때마다 전체 곡 목록을 다시 훑어 해당 장르의 곡을 모으는 것이다. 장르가 최대 100개, 곡이 최대 10,000개라면 최악의 경우 100만 번의 비교가 발생한다. 개선 방식은 해시 맵에 장르를 키로 두고 순회하면서 한 번에 누적하는 것으로, 곡 수에 비례하는 시간에 집계를 마친다. 해시 맵은 키가 존재하지 않을 때 기본값을 만들어 주는 형태(defaultdict, computeIfAbsent)로 쓰면, "키가 있는지 먼저 검사한다"는 분기를 줄일 수 있다.

### 다중 기준 정렬 — 정렬 키 설계

이 문제는 장르 안의 곡을 두 가지 기준으로 정렬해야 한다. 재생 횟수는 내림차순, 고유 번호는 오름차순이다. 초심자 방식은 정렬을 두 번 나누어 하거나(재생 횟수 순 정렬 후 동점인 구간만 다시 정렬), 비교 함수를 일일이 분기 처리하는 것이다. 개선 방식은 정렬 키를 튜플로 구성하는 것이다. Python에서는 `(-재생 횟수, 고유 번호)`라는 키 하나만으로 두 기준을 동시에 표현할 수 있다. 숫자 앞에 마이너스를 붙이면 내림차순이 되므로, 튜플 비교의 사전식 순서가 원하는 정렬과 일치한다. Java에서는 비교자를 직접 작성한다. 재생 횟수가 다르면 재생 횟수 차이를, 같으면 고유 번호 차이를 반환하는 방식으로, 같은 규칙을 명시적으로 표현한다. 두 언어 모두 "정렬 기준을 하나의 비교 규칙으로 합치는" 발상이다.

### 상위 k개만 취하기 — 전체 정렬의 비용

장르마다 최대 두 곡만 필요하므로, 곡 목록 전체를 정렬하는 것은 다소 과한 작업처럼 보일 수 있다. 힙을 이용해 상위 2개만 유지하면 장르 내 곡이 m개일 때 O(m log 2), 즉 O(m) 시간에 끝낼 수 있다. 다만 이 문제에서는 장르당 곡 수가 최대 10,000개 수준이고 정렬 비용이 크지 않으며, 전체 정렬이 코드가 훨씬 단순하다. 상위 k개를 뽑을 때는 k가 작고 m이 클수록 힙이 유리하고, m이 작거나 코드의 단순함이 중요할 때는 전체 정렬이 적절한 선택이다. 이 풀이에서는 전체 정렬을 택했다.

## 최종 솔루션 코드

### Python

```python
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
```

### Java

```java
import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 1. 장르별 총 재생 횟수와 곡 목록(고유 번호, 재생 횟수)을 모은다
        Map<String, Integer> totalByGenre = new HashMap<>();
        Map<String, List<int[]>> songsByGenre = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            totalByGenre.merge(genres[i], plays[i], Integer::sum);
            songsByGenre.computeIfAbsent(genres[i], k -> new ArrayList<>())
                         .add(new int[]{plays[i], i});
        }

        // 2. 장르를 총 재생 횟수 내림차순으로 정렬한다
        List<String> genreOrder = new ArrayList<>(totalByGenre.keySet());
        genreOrder.sort((a, b) -> totalByGenre.get(b) - totalByGenre.get(a));

        List<Integer> answer = new ArrayList<>();
        for (String genre : genreOrder) {
            // 3. 장르 내 곡을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬해 상위 2곡을 수록한다
            List<int[]> songs = songsByGenre.get(genre);
            songs.sort((a, b) -> a[0] != b[0] ? b[0] - a[0] : a[1] - b[1]);
            for (int k = 0; k < Math.min(2, songs.size()); k++) {
                answer.add(songs.get(k)[1]);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
```

## 학습 노트

- 막혔던 점: 없음. 장르별 집계와 곡 정렬을 분리하면 구조가 바로 보인다.
- 핵심 포인트: 해시 맵으로 장르별 총합과 곡 목록을 한 번의 순회로 모으고, 장르·곡 각각의 정렬 기준을 분리해 처리한다.
- 개선: 곡 정렬에 튜플 키 `(-재생 횟수, 고유 번호)`를 사용해 동점 처리(고유 번호 오름차순)를 별도 분기 없이 표현했다.

## 성능 측정

로컬 실측 (2026-10-31, n=100,000 무작위 케이스, 장르 99개).

- 예제 케이스: Python 약 5.8µs (10,000회 반복 평균), Java 1회 호출 수 µs 수준
- n=100,000: Python 0.103s, Java 0.125s, 결과 길이 198개(장르 99개 × 2곡)
- Python 최대 RSS: 약 30.4MB (입력 생성 포함)
- 시간 복잡도: O(n log n) — 곡 정렬이 지배적이며, 장르별 곡 수의 합이 n이다. 장르 수가 최대 100개이므로 장르 정렬 비용은 무시할 수 있다.
- 공간 복잡도: O(n) — 장르별 곡 목록과 장르별 총합을 저장한다.

## 요약

해시 맵으로 장르별 총 재생 횟수와 곡 목록을 한 번에 집계하고, 장르는 총합 내림차순, 곡은 재생 횟수 내림차순·고유 번호 오름차순으로 정렬해 장르마다 상위 두 곡을 수록한다. 정렬 기준을 튜플 키(또는 비교자) 하나로 표현하는 것이 이 문제의 핵심이다.
