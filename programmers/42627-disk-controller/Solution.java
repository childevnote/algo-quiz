import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        // 1. 요청 시각 순으로 정렬 (작업 번호는 원래 인덱스)
        int n = jobs.length;
        int[][] indexed = new int[n][3];
        for (int i = 0; i < n; i++) {
            indexed[i][0] = jobs[i][0]; // 요청 시각
            indexed[i][1] = jobs[i][1]; // 소요 시간
            indexed[i][2] = i;          // 작업 번호
        }
        Arrays.sort(indexed, Comparator.comparingInt(a -> a[0]));

        // 2. 대기 큐: (소요시간, 요청시각, 작업번호) 순 최소 힙
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> {
            if (a[1] != b[1]) return a[1] - b[1];
            if (a[0] != b[0]) return a[0] - b[0];
            return a[2] - b[2];
        });

        int idx = 0;
        int time = 0;
        int total = 0;

        // 3. 모든 작업이 끝날 때까지 시뮬레이션
        while (idx < n || !heap.isEmpty()) {
            // 대기 큐가 비어 있으면 다음 작업 요청 시각으로 점프
            if (heap.isEmpty()) {
                time = Math.max(time, indexed[idx][0]);
            }
            // 현재 시각까지 요청된 작업을 모두 대기 큐에 삽입
            while (idx < n && indexed[idx][0] <= time) {
                heap.offer(indexed[idx]);
                idx++;
            }
            // 우선순위 가장 높은 작업(소요시간 최단) 실행
            int[] job = heap.poll();
            time += job[1];
            total += time - job[0]; // 반환 시간 = 종료 시각 - 요청 시각
        }

        return total / n;
    }
}
