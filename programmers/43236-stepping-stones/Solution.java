import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        // 1. 바위를 위치 순으로 정렬하고 도착지점을 마지막 지점으로 추가
        Arrays.sort(rocks);
        int[] points = Arrays.copyOf(rocks, rocks.length + 1);
        points[rocks.length] = distance;

        // 2. 정답(제거 후 최소 거리)에 대한 이분탐색
        int lo = 1, hi = distance;
        int answer = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            // 3. 최소 거리를 mid로 유지하려면 몇 개의 바위를 제거해야 하는지 셈
            int removed = 0;
            int prev = 0;  // 마지막으로 남긴 지점 (출발지점 0부터)
            for (int rock : points) {
                if (rock - prev < mid) {
                    removed++;  // 간격이 부족하면 이 바위를 제거
                } else {
                    prev = rock;  // 간격이 충분하면 이 바위를 남김
                }
            }
            // 4. 제거 개수가 n 이하이면 mid는 달성 가능 -> 더 큰 값 시도
            if (removed <= n) {
                answer = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return answer;
    }
}
