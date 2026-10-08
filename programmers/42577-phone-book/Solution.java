// 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577
// 풀이일: 2026-10-08
// Lv.2 · 해시 — 전화번호 목록

import java.util.Arrays;

public class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);  // ① 사전식 정렬: 접두어 관계는 정렬 후 반드시 인접해 나타난다
        for (int i = 0; i < phone_book.length - 1; i++) {
            // ② 앞 번호가 뒷 번호의 접두어인지 확인
            if (phone_book[i + 1].startsWith(phone_book[i])) return false;
        }
        return true;
    }
}
