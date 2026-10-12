import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int[] priorities, int location) {
        // {원래 위치, 우선순위} 쌍을 담는 실행 대기 큐
        Queue<int[]> queue = new ArrayDeque<>();
        // 1. 우선순위별 남은 개수 (우선순위는 1~9로 고정)
        int[] freq = new int[10];
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
            freq[priorities[i]]++;
        }
        // 2. 현재 큐에 남아 있는 최대 우선순위
        int highest = 9;
        while (freq[highest] == 0) highest--;
        int order = 0;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int idx = cur[0], p = cur[1];
            if (p < highest) {
                // 3. 더 높은 우선순위가 남아 있으면 맨 뒤로 보냄
                queue.offer(cur);
            } else {
                // 4. 실행 확정 (다시 큐에 넣지 않음)
                order++;
                freq[p]--;
                if (idx == location) return order;
                // 5. 실행된 우선순위가 소진되면 최대값 갱신
                while (highest > 0 && freq[highest] == 0) highest--;
            }
        }
        return order;
    }
}
