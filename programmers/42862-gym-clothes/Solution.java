import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> need = new HashSet<>();
        Set<Integer> give = new HashSet<>();
        for (int l : lost) need.add(l);
        for (int r : reserve) give.add(r);
        Set<Integer> lostOrig = new HashSet<>(need);
        // 1. 자급자족 학생 제외: lost와 reserve에 모두 있으면 스스로 해결
        need.removeAll(give);
        // 2. 대여 가능한 여벌만 남기기
        give.removeAll(lostOrig);
        int[] arr = need.stream().mapToInt(i -> i).toArray();
        // 3. 번호가 작은 학생부터
        Arrays.sort(arr);
        for (int l : arr) {
            // 4. 앞번호 이웃에게 우선 대여
            if (give.contains(l - 1)) give.remove(l - 1);
            // 5. 없으면 뒷번호 이웃에게 대여
            else if (give.contains(l + 1)) give.remove(l + 1);
            // 6. 빌리지 못하면 수업에서 제외
            else n--;
        }
        return n;
    }
}
