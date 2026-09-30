# 완주하지 못한 선수

- 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42576
- 레벨: Lv.1 / 카테고리: 해시

## 문제 핵심 요약

마라톤 참가자 명단(participant)과 완주자 명단(completion)이 주어질 때, 완주하지 못한 1명의 이름을 구하는 문제.

- 참가자 수는 1명 이상 100,000명 이하
- completion의 길이는 participant보다 1 작음
- 참가자 중 동명이인이 있을 수 있음

입출력 예:

| participant | completion | return |
|---|---|---|
| ["leo", "kiki", "eden"] | ["eden", "kiki"] | "leo" |
| ["mislav", "stanko", "mislav", "ana"] | ["stanko", "ana", "mislav"] | "mislav" |

## 학습 노트

- 막혔던 점: 리스트에서 찾아 지우는 방식을 떠올렸으나 n=100,000일 때 O(n²)이라 시간 초과가 우려됨. 힌트 후 해시맵으로 빈도를 세는 방향으로 전환.
- 핵심 포인트: 이름 → 등장 횟수를 해시맵에 누적하면 전체를 한 번씩만 훑어 O(n)에 해결. 동명이인도 횟수로 처리돼 별도 분기 불필요.
- 개선: `Counter.subtract`, `getOrDefault`를 써서 초기화 분기 없이 간결하게 작성.
