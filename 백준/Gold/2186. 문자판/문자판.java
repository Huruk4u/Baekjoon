import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N, M, K;

    private static char[][] matrix;

    private static int[][][] dp;

    private static char[] word;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        matrix = new char[N][M];
        for (int i = 0; i < N; i++) matrix[i] = br.readLine().toCharArray();

        word = br.readLine().toCharArray();
        dp = new int[N][M][word.length];
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) Arrays.fill(dp[y][x], -1);
        }

        // O(10000)
        int answer = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (matrix[y][x] != word[0]) continue;
                answer += dfs(y, x, 0);
            }
        }

        System.out.println(answer);
        br.close();
    }

    private static int dfs(int cy, int cx, int depth) {
        if (depth == word.length - 1) return 1;
        if (dp[cy][cx][depth] != -1) return dp[cy][cx][depth];

        dp[cy][cx][depth] = 0;

        for (int i = 0; i < 4; i++) {
            for (int k = 1; k <= K; k++) {
                int ny = cy + dy[i] * k;
                int nx = cx + dx[i] * k;
                if (!inRange(ny, nx) || matrix[ny][nx] != word[depth+1]) continue;
                dp[cy][cx][depth] += dfs(ny, nx, depth+1);
            }
        }

        return dp[cy][cx][depth];
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < M);
    }
}
