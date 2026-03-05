import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int MOD = 1000000000;

        int[][] dp = new int[N+1][K+1];
        for (int i = 0; i < N+1; i++) dp[i][1] = 1;
        for (int i = 1; i < K+1; i++) dp[1][i] = i;

        for (int i = 2; i < N+1; i++) {
            for (int j = 2; j < K+1; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }
        System.out.println(dp[N][K]);

        br.close();
    }
}
