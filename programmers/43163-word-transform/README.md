# 단어 변환

- 문제: [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)
- 레벨: Lv.3
- 카테고리: DFS/BFS
- 날짜: 2026-11-09

## 문제 핵심 요약

두 단어 `begin`과 `target`, 그리고 단어 집합 `words`가 주어진다. 한 번에 알파벳 한 글자만 바꿀 수 있고, 바꿀 때마다 `words` 안에 있는 단어여야 한다. `begin`에서 `target`까지 도달하는 가장 짧은 변환 단계 수를 구한다.

핵심 제한사항:

- 모든 단어의 길이는 같고 3 이상 10 이하이다.
- `words`의 단어 수는 3 이상 50 이하이며 중복이 없다.
- `begin`과 `target`은 다르다.
- `target`이 `words`에 없거나 도달할 수 없으면 0을 반환한다.

입출력 예:

| begin | target | words | return |
| --- | --- | --- | --- |
| "hit" | "cog" | ["hot", "dot", "dog", "lot", "log", "cog"] | 4 |
| "hit" | "cog" | ["hot", "dot", "dog", "lot", "log"] | 0 |

## 문제 분석 및 핵심 로직

이 문제는 단어들을 정점, 한 글자만 다른 단어 쌍을 간선으로 하는 그래프에서 `begin`에서 `target`까지의 최단 경로 길이를 묻는 문제이다. 간선의 가중치가 모두 1이므로 너비 우선 탐색(BFS)이 처음 `target`에 도달하는 순간이 곧 최단 단계 수이다.

핵심 로직은 다음과 같다.

1. `target`이 `words`에 없으면 변환이 불가능하므로 0을 바로 반환한다. 이 검사가 없으면 BFS를 끝까지 돌고 나서야 0을 알 수 있다.
2. 큐에 `(단어, 지금까지의 단계 수)`를 넣고 BFS를 시작한다. 시작 단어 `begin`은 단계 수 0이다.
3. 현재 단어에서 한 글자씩 바꿔본다. 각 자리마다 알파벳 26개를 대입해 만든 후보 단어가 `words` 안에 있고 아직 방문하지 않았다면 큐에 넣는다.
4. 큐에서 꺼낸 단어가 `target`이면 그때의 단계 수가 답이다. BFS는 단계 수 오름차순으로 탐색하므로 처음 도달한 경로가 최단이다.
5. 큐가 비워질 때까지 `target`에 닿지 못하면 변환이 불가능하므로 0을 반환한다.

## 개념별 심층 설명

### 1. BFS가 최단 경로를 보장하는 이유

초심자 방식은 DFS로 모든 변환 경로를 끝까지 따라가며 가장 짧은 경로를 기록하는 것이다. 이 방식은 동작하지만, 이미 더 긴 경로를 탐색한 뒤에도 더 짧은 경로가 남아 있을 수 있어 전체를 다 봐야 한다.

BFS는 시작점에서 거리가 1인 단어들을 전부 처리한 뒤 거리 2인 단어들로 넘어가는 식으로, 단계 수 순서대로 탐색한다. 그래서 `target`을 처음 만나는 순간이 그보다 짧은 경로는 존재하지 않는다는 뜻이고, 그 즉시 탐색을 멈춰도 된다. 간선 가중치가 모두 1일 때만 성립하는 성질이다.

### 2. 이웃 단어 생성: 한 글자씩 바꿔보기 vs 전체 비교

초심자 방식은 현재 단어와 `words`의 모든 단어를 한 글자씩 비교해 다른 글자가 1개인지 확인하는 것이다. 단어 길이를 L, 단어 수를 N이라 하면 한 정점마다 O(N × L)의 비교가 필요하다.

개선 방식은 현재 단어의 각 자리를 26개 알파벳으로 바꿔 후보 단어를 직접 만들고, 그 단어가 `words` 안에 있는지 해시 집합으로 확인하는 것이다. 한 정점마다 26 × L개의 후보만 만들면 되고, 집합 조회는 평균 O(1)이다. 단어 수 N이 커질수록 이 방식이 유리하다. 이 문제의 제한(N ≤ 50)에서는 두 방식 모두 충분하지만, 단어 수가 늘어나는 상황을 고려하면 후보 생성 방식이 확장성이 좋다.

### 3. visited 관리와 중복 탐색 방지

한 단어를 여러 경로로 다시 방문하면 큐가 불필요하게 커지고, 같은 단어를 반복해서 탐색하게 된다. 방문한 단어는 큐에 넣는 시점에 `visited`에 기록한다. 큐에서 꺼낼 때가 아니라 넣을 때 기록해야 같은 단어가 여러 번 큐에 들어가는 것을 막을 수 있다.

### 4. `target` 부재 검사를 먼저 하는 이유

`target`이 `words`에 없는 경우는 변환이 원천적으로 불가능하다. 이를 BFS 전에 한 번의 집합 조회로 걸러내면, 도달할 수 없는 탐색을 끝까지 돌 필요가 없어진다. 이 문제는 예제 2번이 정확히 이 경우에 해당한다.

## 최종 솔루션 코드

### Python

```python
from collections import deque


def solution(begin, target, words):
    word_set = set(words)
    # 1. target이 words에 없으면 변환 자체가 불가능하다.
    if target not in word_set:
        return 0

    # 2. BFS: 큐에 (단어, 지금까지의 단계 수)를 넣고 한 글자씩 바꿔가며 탐색한다.
    queue = deque([(begin, 0)])
    visited = {begin}
    length = len(begin)

    while queue:
        word, steps = queue.popleft()
        # 3. target에 도달하면 그때의 단계 수가 최단 변환 횟수이다.
        if word == target:
            return steps
        # 4. 각 자리마다 26개 알파벳으로 바꿔본 뒤 words 안에 있는 단어만 다음 후보로 삼는다.
        for i in range(length):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == word[i]:
                    continue
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in word_set and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

    # 5. 큐를 다 비워도 target에 닿지 못하면 변환 불가.
    return 0
```

### Java

```java
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Set<String> wordSet = new HashSet<>();
        for (String w : words) wordSet.add(w);
        // 1. target이 words에 없으면 변환 자체가 불가능하다.
        if (!wordSet.contains(target)) return 0;

        // 2. BFS: 큐에 (단어, 지금까지의 단계 수)를 넣고 한 글자씩 바꿔가며 탐색한다.
        Queue<String[]> queue = new ArrayDeque<>();
        queue.offer(new String[]{begin, "0"});
        Set<String> visited = new HashSet<>();
        visited.add(begin);
        int length = begin.length();

        while (!queue.isEmpty()) {
            String[] cur = queue.poll();
            String word = cur[0];
            int steps = Integer.parseInt(cur[1]);
            // 3. target에 도달하면 그때의 단계 수가 최단 변환 횟수이다.
            if (word.equals(target)) return steps;
            // 4. 각 자리마다 26개 알파벳으로 바꿔본 뒤 words 안에 있는 단어만 다음 후보로 삼는다.
            for (int i = 0; i < length; i++) {
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    if (ch == word.charAt(i)) continue;
                    String nxt = word.substring(0, i) + ch + word.substring(i + 1);
                    if (wordSet.contains(nxt) && !visited.contains(nxt)) {
                        visited.add(nxt);
                        queue.offer(new String[]{nxt, String.valueOf(steps + 1)});
                    }
                }
            }
        }

        // 5. 큐를 다 비워도 target에 닿지 못하면 변환 불가.
        return 0;
    }
}
```

## 성능 측정

로컬 실측 결과 (2026-11-09):

| 측정 | Python | Java |
| --- | --- | --- |
| 예제 케이스 (10,000회 평균) | 약 107 μs/회 | — |
| 스케일 테스트 (단어 100,192개) | 약 0.033초 | 약 0.098초 |
| 스케일 테스트 피크 메모리 | 약 28 MB (프로세스 전체) | — |

스케일 테스트는 문제 제한(words ≤ 50개)을 크게 넘는 합성 데이터이다. 길이 10인 무작위 단어 100,000개에 한 글자씩 바꿔 이어지는 200단계 경로를 섞어, 도달 가능한 최단 경로(178단계)를 측정했다. 정확성은 한 글자 차이 여부를 직접 비교하는 별도의 참조 BFS와 대조해 확인했다.

- 시간 복잡도: O(26 × L × V). V는 방문한 단어 수, L은 단어 길이이다. 각 정점에서 26 × L개의 후보를 만들고 해시 집합으로 조회한다.
- 공간 복잡도: O(N × L). 단어 집합, 방문 집합, 큐가 단어 수에 비례한다.

## 요약

- 간선 가중치가 1인 그래프의 최단 경로는 BFS로 구한다. 처음 `target`에 도달한 순간이 곧 답이다.
- 이웃 단어는 `words` 전체와 비교하는 대신 각 자리를 26개 알파벳으로 바꿔 직접 생성하고 해시 집합으로 조회한다.
- `target`이 `words`에 없으면 0을 바로 반환하고, 큐를 다 비워도 닿지 못하면 0을 반환한다.
- 학습 노트: 이 문제는 DFS로 모든 경로를 탐색하는 대신 BFS의 단계별 탐색 순서를 이용해 최단 경로를 보장한다는 점이 핵심이다. 방문 기록은 큐에 넣는 시점에 남겨 중복 탐색을 막는다.
