import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0;
        int right = people.length - 1;
        int boats = 0;
        while (left <= right) {
            // 1. 가장 가벼운 사람과 가장 무거운 사람을 한 배에 태울 수 있으면 함께 태운다
            if (people[left] + people[right] <= limit) {
                left++;
            }
            // 2. 가장 무거운 사람은 어느 경우든 이번 배에 태운다 (혼자 타거나, 짝과 함께)
            right--;
            boats++;
        }
        return boats;
    }
}
