import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;

    private static int[][] riceCakes;

    private static int[][] visited;

    private static boolean flag = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine().trim());
        riceCakes = new int[N+1][10]; // riceCakes[날짜][떡의 종류 유무]

        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int k = Integer.parseInt(st.nextToken()); // 아직 k의 쓰임새는 모르겠다.
            while (st.hasMoreTokens()) {
                riceCakes[i][Integer.parseInt(st.nextToken())] = 1;
            }
        }

        visited = new int[N+1][10];

        dfs(0, 0, new int[N+1]);
        if (!flag) System.out.println(-1);

        br.close();
    }

    private static void dfs(int day, int curr, int[] path) {
        if (flag) return;

        if (day == N) {
            for (int i = 1; i < N+1; i++) System.out.println(path[i]);
            flag = true;
            return;
        }

        for (int next = 1; next < 10; next++) {
            if (flag) break;
            if (curr == next) continue;
            if (riceCakes[day+1][next] == 0 || visited[day+1][next] == 1) continue;

            visited[day+1][next] = 1;
            path[day+1] = next;
            dfs(day+1, next, path);
        }
        return;
    }
}
