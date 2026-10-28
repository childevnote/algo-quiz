class Solution {
    public String solution(String number, int k) {
        // 1. 단조 감소 스택: char 배열을 스택으로 쓰고, 현재 숫자보다 작은
        //    스택 상단은 제거 기회(k)가 남아 있는 한 제거한다.
        char[] stack = new char[number.length()];
        int top = 0;
        for (int i = 0; i < number.length(); i++) {
            char digit = number.charAt(i);
            while (k > 0 && top > 0 && stack[top - 1] < digit) {
                top--;
                k--;
            }
            stack[top++] = digit;
        }
        // 2. 제거 기회가 남았으면(전체가 내림차순인 경우) 뒤에서 자른다.
        top -= k;
        // 3. 남은 구간을 문자열로 만든다. 순서가 곧 원래 상대 순서이다.
        return new String(stack, 0, top);
    }
}
