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
