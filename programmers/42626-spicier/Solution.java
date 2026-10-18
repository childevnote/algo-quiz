import java.util.PriorityQueue;

// 더 맵게 — https://school.programmers.co.kr/learn/courses/30/lessons/42626
// 2026-10-18 (18:00 자동 풀이)
class Solution {
    public int solution(int[] scoville, int K) {
        // 1. 전체를 최소 힙(PriorityQueue)으로
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int s : scoville) pq.offer((long) s);

        int answer = 0;
        // 2. 가장 안 매운 게 K 미만이면 계속 섞음
        while (!pq.isEmpty() && pq.peek() < K) {
            // 3. 섞을 수 없으면 -1
            if (pq.size() < 2) return -1;
            // 4. 가장 안 매운 두 개를 꺼내 5. 섞은 음식 투입
            long first = pq.poll();
            long second = pq.poll();
            pq.offer(first + 2 * second);
            answer++;
        }
        return answer;
    }
}
