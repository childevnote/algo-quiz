import java.util.Arrays;

class Solution {
    public long solution(long n) {
        // 1. n을 문자열로 바꿔 각 자릿수를 문자로 만든다.
        // 2. 자릿수 문자를 오름차순으로 정렬한다.
        // 3. 뒤에서부터 이어 붙이면 내림차순이 된다.
        // n은 최대 8,000,000,000이므로 long으로 받는다.
        char[] digits = String.valueOf(n).toCharArray();
        Arrays.sort(digits);
        StringBuilder sb = new StringBuilder(digits.length);
        for (int i = digits.length - 1; i >= 0; i--) {
            sb.append(digits[i]);
        }
        return Long.parseLong(sb.toString());
    }
}
