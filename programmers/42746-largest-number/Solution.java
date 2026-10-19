import java.util.Arrays;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/42746
 * 프로그래머스 42746 - 가장 큰 수 (Lv.2, 정렬)
 * 작성일: 2026-10-19 (18:00 자동 풀이)
 */
class Solution {
    public String solution(int[] numbers) {
        // 1. 숫자를 문자열로 변환 (이어 붙이기 비교를 위해)
        String[] strs = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strs[i] = String.valueOf(numbers[i]);
        }
        // 2. (a+b)와 (b+a) 중 더 큰 쪽을 앞에 오게 정렬
        Arrays.sort(strs, (a, b) -> (b + a).compareTo(a + b));
        // 3. 모두 0인 경우 "0"을 반환 (000... 방지)
        if (strs[0].equals("0")) {
            return "0";
        }
        // 4. 이어 붙여 반환
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s);
        }
        return sb.toString();
    }
}
