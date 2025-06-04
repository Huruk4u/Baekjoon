import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {

    private int N, M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ipt;

        /////////////////////////////////////// input
        ipt = br.readLine().trim().split(" ");
        int N = Integer.parseInt(ipt[0]);
        int M = Integer.parseInt(ipt[1]);

        int[][] matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            ipt = br.readLine().trim().split("");
            for (int j = 0; j < M; j++) matrix[i][j] = Integer.parseInt(ipt[j]);
        }
        /////////////////////////////////////// input

        int[][] dp = new int[N][M];
        // 변두리에 있는 값들 최소 dp 매겨주기
        // 밑변 처리
        for (int x = 0; x < M; x++) {
            if (matrix[N-1][x] == 0) continue;
            dp[N-1][x] = 1;
        }

        // 오른쪽 변 처리
        for (int y = 0; y < N; y++) {
            if (matrix[y][M-1] == 0) continue;
            dp[y][M-1] = 1;
        }

        for (int y = N-2; y >= 0; y--) {
            for (int x = M-2; x >=0; x--) {
                if (matrix[y][x] == 0) continue;
                // y, x좌표를 기준으로 아래, 대각, 우측 방향에 있는 최소 정사각형 크기
                int minRectSize = Collections.min(Arrays.asList(dp[y+1][x], dp[y][x+1], dp[y+1][x+1]));
                dp[y][x] = minRectSize + 1;
            }
        }

        int answer = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) answer = Math.max(answer, dp[y][x]);
        }

        System.out.println(answer * answer);
        br.close();
    }

}
