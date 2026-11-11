import java.util.*;

class Solution {
    public String[] solution(String[][] tickets) {
        Map<String, List<String>> graph = new HashMap<>();
        // 1. 출발 공항별로 도착 공항 목록을 만든다.
        for (String[] ticket : tickets) {
            graph.computeIfAbsent(ticket[0], k -> new ArrayList<>()).add(ticket[1]);
        }
        // 2. 알파벳 역순으로 정렬해 두면 removeLast()로 가장 작은 도착 공항을 꺼낼 수 있다.
        for (List<String> dsts : graph.values()) {
            dsts.sort(Collections.reverseOrder());
        }

        List<String> route = new ArrayList<>();
        Deque<String> stack = new ArrayDeque<>();
        stack.push("ICN");
        // 3. Hierholzer 알고리즘: 더 이상 갈 간선이 없을 때만 경로에 확정한다.
        while (!stack.isEmpty()) {
            List<String> dsts = graph.getOrDefault(stack.peek(), List.of());
            while (!dsts.isEmpty()) {
                stack.push(dsts.remove(dsts.size() - 1));
                dsts = graph.getOrDefault(stack.peek(), List.of());
            }
            route.add(stack.pop());
        }
        // 4. 확정 순서가 역순이므로 뒤집으면 ICN에서 시작하는 전체 경로가 된다.
        Collections.reverse(route);
        return route.toArray(new String[0]);
    }
}
