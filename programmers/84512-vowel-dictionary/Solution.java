class Solution {
    public int solution(String word) {
        String vowels = "AEIOU";
        // 1. 자기 자신과 조상 단어 수만큼 기본 카운트 (길이만큼)
        int answer = word.length();
        for (int i = 0; i < word.length(); i++) {
            // 2. 현재 자리보다 작은 모음 개수
            int idx = vowels.indexOf(word.charAt(i));
            // 3. 그 모음 아래에 달린 서브트리 단어 수: 1 + 5 + ... + 5^(4-i)
            int subtree = (pow5(5 - i) - 1) / 4;
            // 4. 건너뛴 서브트리만큼 더한다
            answer += idx * subtree;
        }
        return answer;
    }

    private int pow5(int n) {
        int r = 1;
        for (int i = 0; i < n; i++) r *= 5;
        return r;
    }
}
