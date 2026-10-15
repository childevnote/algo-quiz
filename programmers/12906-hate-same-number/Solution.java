import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int x : arr) {
            // 1. 결과의 마지막 값과 현재 값이 다를 때만 추가 (연속 중복 제거)
            if (list.isEmpty() || list.get(list.size() - 1) != x) {
                list.add(x);
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}
