import java.util.*;

class Solution {
    public int solution(int[] arrows) {
        // 방향 0~7: 0=위, 1=오른쪽 위, 2=오른쪽, 3=오른쪽 아래,
        //          4=아래, 5=왼쪽 아래, 6=왼쪽, 7=왼쪽 위
        int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
        int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};

        // 정점과 간선을 기록한다. 대각선 이동이 간선 중간에서
        // 교차하는 경우를 잡기 위해 한 칸 이동을 절반씩 두 번 나눈다.
        Set<String> visitedV = new HashSet<>();
        Set<String> visitedE = new HashSet<>();
        visitedV.add("0,0");
        int x = 0, y = 0;
        int rooms = 0;

        for (int a : arrows) {
            for (int i = 0; i < 2; i++) {  // 절반 이동 2회
                int nx = x + dx[a], ny = y + dy[a];
                String from = x + "," + y;
                String to = nx + "," + ny;
                String edge = from.compareTo(to) < 0 ? from + "|" + to : to + "|" + from;
                if (visitedV.contains(to) && !visitedE.contains(edge)) {
                    // 이미 들른 정점에 새 간선으로 도착하면 방 하나가 닫힌다
                    rooms++;
                }
                visitedV.add(to);
                visitedE.add(edge);
                x = nx;
                y = ny;
            }
        }
        return rooms;
    }
}
