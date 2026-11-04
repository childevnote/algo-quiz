import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        // 1. 진출 지점 오름차순으로 정렬 — 카메라 위치의 기준이 된다
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

        int count = 0;
        int camera = Integer.MIN_VALUE; // 2. 가장 최근에 설치한 카메라의 위치
        boolean hasCamera = false;
        for (int[] r : routes) {
            // 3. 기존 카메라가 이 차량의 구간을 커버하지 못하면
            //    이 차량의 진출 지점에 새 카메라를 설치한다
            if (!hasCamera || camera < r[0] || camera > r[1]) {
                camera = r[1];
                hasCamera = true;
                count++;
            }
        }
        return count;
    }
}
