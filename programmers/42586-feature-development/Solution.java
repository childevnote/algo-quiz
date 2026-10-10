class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = progresses.length;
        // 1. 각 작업이 완성되기까지 남은 일수 계산 (올림)
        int[] days = new int[n];
        for (int i = 0; i < n; i++) {
            days[i] = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
        }
        // 2. 앞 작업의 배포일을 넘지 못하면 함께 배포, 넘으면 새 배포
        java.util.List<Integer> list = new java.util.ArrayList<>();
        int curDay = days[0], count = 1;
        for (int i = 1; i < n; i++) {
            if (days[i] <= curDay) {
                count++;
            } else {
                list.add(count);
                curDay = days[i];
                count = 1;
            }
        }
        list.add(count);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}
