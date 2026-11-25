class Solution {
    public int[] solution(long n) {
        // 1. 10으로 나눈 나머지가 일의 자리 숫자이다.
        // 2. 나머지를 순서대로 모으면 뒤집힌 자릿수 배열이 된다.
        // 3. 10으로 나눈 몫으로 자리수를 한 칸씩 줄여 나간다.
        // n은 최대 10,000,000,000이므로 long으로 받는다.
        String s = String.valueOf(n);
        int[] answer = new int[s.length()];
        int idx = 0;
        while (n > 0) {
            answer[idx++] = (int) (n % 10);
            n /= 10;
        }
        return answer;
    }
}
