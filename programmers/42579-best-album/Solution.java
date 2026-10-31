import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 1. 장르별 총 재생 횟수와 곡 목록(고유 번호, 재생 횟수)을 모은다
        Map<String, Integer> totalByGenre = new HashMap<>();
        Map<String, List<int[]>> songsByGenre = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            totalByGenre.merge(genres[i], plays[i], Integer::sum);
            songsByGenre.computeIfAbsent(genres[i], k -> new ArrayList<>())
                         .add(new int[]{plays[i], i});
        }

        // 2. 장르를 총 재생 횟수 내림차순으로 정렬한다
        List<String> genreOrder = new ArrayList<>(totalByGenre.keySet());
        genreOrder.sort((a, b) -> totalByGenre.get(b) - totalByGenre.get(a));

        List<Integer> answer = new ArrayList<>();
        for (String genre : genreOrder) {
            // 3. 장르 내 곡을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬해 상위 2곡을 수록한다
            List<int[]> songs = songsByGenre.get(genre);
            songs.sort((a, b) -> a[0] != b[0] ? b[0] - a[0] : a[1] - b[1]);
            for (int k = 0; k < Math.min(2, songs.size()); k++) {
                answer.add(songs.get(k)[1]);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
