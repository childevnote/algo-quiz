class Solution {
    public int solution(int[][] sizes) {
        int maxW = 0;
        int maxH = 0;
        for (int[] s : sizes) {
            // 1. 각 명함을 회전시켜 긴 쪽을 가로로 눕히기
            int w = Math.max(s[0], s[1]);
            int h = Math.min(s[0], s[1]);
            // 2. 지금까지 본 명함 중 가장 긴 가로/세로 갱신
            maxW = Math.max(maxW, w);
            maxH = Math.max(maxH, h);
        }
        // 3. 가장 작은 지갑의 크기
        return maxW * maxH;
    }
}
