import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;

    private static char[][] matrix;

    private static boolean[][] visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        matrix = new char[N][M];
        for (int i = 0; i < N; i++) matrix[i] = br.readLine().toCharArray();

        visited = new boolean[N][M];
        boolean answer = false;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (visited[y][x]) continue;
                visited[y][x] = true;
                answer |= dfs(y, x, -1, -1);
            }
        }
        if (answer) System.out.println("Yes"); 
        else System.out.println("No");

        br.close();
    }

    private static boolean dfs(int cy, int cx, int py, int px) {
        boolean rtn = false;
        for (int i = 0; i < 4; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];
            if (!inRange(ny, nx) || matrix[ny][nx] != matrix[cy][cx]) continue;
            if (ny == py && nx == px) continue;
            if (visited[ny][nx]) return true;
            visited[ny][nx] = true;
            rtn |= dfs(ny, nx, cy, cx);
        }
        return rtn;
    }

    private static boolean inRange(int y, int x) {
        return 0 <= y && y < N && 0 <= x && x < M;
    }
}
