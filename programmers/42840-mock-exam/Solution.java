// 프로그래머스 42840 모의고사 (https://school.programmers.co.kr/learn/courses/30/lessons/42840)
// 풀이 날짜: 2026-10-16

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int[] solution(int[] answers) {
        // ① 각 수포자의 찍기 패턴 (반복 주기)
        int[][] patterns = {
            {1, 2, 3, 4, 5},                  // 1번: 길이 5
            {2, 1, 2, 3, 2, 4, 2, 5},         // 2번: 길이 8
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5},   // 3번: 길이 10
        };

        // ② 각 패턴을 answers 길이에 맞춰 순환하며 맞힌 개수 세기
        int[] scores = new int[3];
        for (int j = 0; j < 3; j++) {
            int m = patterns[j].length;
            for (int i = 0; i < answers.length; i++) {
                if (answers[i] == patterns[j][i % m]) {
                    scores[j]++;
                }
            }
        }

        // ③ 최고점과 동점자를 찾아 오름차순 반환
        int best = Math.max(scores[0], Math.max(scores[1], scores[2]));
        List<Integer> winners = new ArrayList<>();
        for (int j = 0; j < 3; j++) {
            if (scores[j] == best) winners.add(j + 1);
        }
        return winners.stream().mapToInt(Integer::intValue).toArray();
    }
}
