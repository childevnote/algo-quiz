import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;
        // 오름차순 정렬 후 뒤에서부터: n-i개의 논문이 citations[i]회 이상 인용됨
        for (int i = 0; i < n; i++) {
            int papers = n - i;
            if (citations[i] >= papers) {
                h = papers;
                break;
            }
        }
        return h;
    }
}
