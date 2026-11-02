import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();  // 1. 최솟값 꺼내기용 최소 힙
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(java.util.Comparator.reverseOrder());  // 2. 최댓값 꺼내기용 최대 힙
        Map<Integer, Integer> count = new HashMap<>();  // 3. 값이 실제로 큐에 몇 개 남아 있는지 세는 맵

        for (String op : operations) {
            String[] parts = op.split(" ");
            int num = Integer.parseInt(parts[1]);

            if (parts[0].equals("I")) {
                // 삽입: 두 힙 모두에 넣고 개수 기록
                minHeap.offer(num);
                maxHeap.offer(num);
                count.put(num, count.getOrDefault(num, 0) + 1);
            } else if (num == 1) {
                // 4. 최댓값 삭제: 이미 삭제된 stale 원소를 건너뛰고 poll
                while (!maxHeap.isEmpty() && count.getOrDefault(maxHeap.peek(), 0) == 0) {
                    maxHeap.poll();
                }
                if (!maxHeap.isEmpty()) {
                    int v = maxHeap.poll();
                    count.put(v, count.get(v) - 1);
                }
            } else {  // num == -1
                // 5. 최솟값 삭제: 같은 방식으로 최소 힙에서 poll
                while (!minHeap.isEmpty() && count.getOrDefault(minHeap.peek(), 0) == 0) {
                    minHeap.poll();
                }
                if (!minHeap.isEmpty()) {
                    int v = minHeap.poll();
                    count.put(v, count.get(v) - 1);
                }
            }
        }

        // 6. 양쪽 힙의 top을 stale 원소 없이 정리
        while (!maxHeap.isEmpty() && count.getOrDefault(maxHeap.peek(), 0) == 0) {
            maxHeap.poll();
        }
        while (!minHeap.isEmpty() && count.getOrDefault(minHeap.peek(), 0) == 0) {
            minHeap.poll();
        }

        if (maxHeap.isEmpty()) {
            return new int[]{0, 0};
        }
        return new int[]{maxHeap.peek(), minHeap.peek()};
    }
}
