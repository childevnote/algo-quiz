import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        // 1. 종류별 의상 개수를 센다
        Map<String, Integer> counts = new HashMap<>();
        for (String[] c : clothes) {
            counts.put(c[1], counts.getOrDefault(c[1], 0) + 1);
        }
        // 2. 종류마다 (개수 + 1)가지 선택지(해당 종류를 안 입는 경우 포함)를 곱하고,
        //    모든 종류를 안 입는 1가지 경우를 뺀다
        int answer = 1;
        for (int c : counts.values()) {
            answer *= (c + 1);
        }
        return answer - 1;
    }
}
