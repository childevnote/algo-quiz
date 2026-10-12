class Solution {
    boolean solution(String s) {
        int balance = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                balance++;
            } else {
                if (--balance < 0) {
                    return false;
                }
            }
        }
        return balance == 0;
    }
}
