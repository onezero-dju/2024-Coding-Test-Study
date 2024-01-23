package 일영_코테_준비;

import java.util.*;

public class BJ_2210 {
    static int[][] map = new int[5][5];
    static Set<String> set = new HashSet<>();

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                map[i][j] = sc.nextInt();
            }
        }

        //dfs 함수를 사용해 결과 출력
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                dfs(i, j, String.valueOf(map[i][j]));
            }
        }
        System.out.println(set.size());
    }

    static void dfs(int x, int y, String s) {
        if (s.length() == 6) {
            set.add(s);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
                dfs(nx, ny, s + map[nx][ny]);
            }
        }
    }
}
