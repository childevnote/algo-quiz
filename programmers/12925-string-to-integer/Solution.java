class Solution {
    public int solution(String s) {
        // 1. 맨앞 부호를 확인한다. '-'이면 음수, '+'이거나 없으면 양수이다.
        // 2. 숫자 자릿수를 왼쪽부터 한 자리씩 누적한다: result = result * 10 + digit.
        //    '0' 문자의 코드값을 빼면 문자 '3'은 숫자 3이 된다.
        // 3. 음수이면 부호를 뒤집어 반환한다.
        boolean negative = s.charAt(0) == '-';
        int start = (s.charAt(0) == '+' || s.charAt(0) == '-') ? 1 : 0;
        int result = 0;
        for (int i = start; i < s.length(); i++) {
            result = result * 10 + (s.charAt(i) - '0');
        }
        return negative ? -result : result;
    }
}
