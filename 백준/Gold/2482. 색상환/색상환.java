import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    private static int MOD = 1000000003;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().trim());
        int K = Integer.parseInt(br.readLine().trim());

        int[][] dp = new int[N+1][N+1];
        for (int i = 1; i < N+1; i++) {
            dp[i][0] = 1;
            dp[i][1] = i;
        }

        for (int i = 3; i < N+1; i++) {
            for (int j = 2; j <= (i + 1) / 2; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % MOD;
            }
        }
        System.out.println((dp[N-3][K-1] + dp[N-1][K]) % MOD);

        br.close();
    }
}
