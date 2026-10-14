import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<int[]> bridge = new ArrayDeque<>(); // {트럭 무게, 다리를 완전히 나가는 시각}
        int total = 0; // 다리 위 트럭들의 무게 합
        int time = 0;
        int idx = 0;

        while (idx < truck_weights.length || !bridge.isEmpty()) {
            time++;
            // 1. 나가는 시각이 된 트럭을 다리에서 내린다
            if (!bridge.isEmpty() && bridge.peekFirst()[1] == time) {
                total -= bridge.pollFirst()[0];
            }
            // 2. 대기 중인 첫 트럭이 진입 조건(빈자리, 무게 여유)을 만족하면 올린다
            if (idx < truck_weights.length
                    && bridge.size() < bridge_length
                    && total + truck_weights[idx] <= weight) {
                int w = truck_weights[idx++];
                bridge.addLast(new int[]{w, time + bridge_length});
                total += w;
            }
        }
        return time;
    }
}
