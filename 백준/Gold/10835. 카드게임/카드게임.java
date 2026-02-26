import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    private static int[][] dp;

    private static int[] leftCards, rightCards;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine().trim());

        leftCards = new int[N+1];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) leftCards[i] = Integer.parseInt(st.nextToken());

        rightCards = new int[N+1];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) rightCards[i] = Integer.parseInt(st.nextToken());

        dp = new int[N+1][N+1];
        for (int i = 0; i < N+1; i++) Arrays.fill(dp[i], -1);
        System.out.println(solve(0, 0));

        br.close();
    }

    private static int solve(int left, int right) {
        if (dp[left][right] != -1) return dp[left][right];
        if (left == N && right == N) return 0;

        dp[left][right] = 0;
        if (left < N) {
            dp[left][right] = Integer.max(dp[left][right], solve(left+1, right));
        }
        if (left < N && right < N) {
            dp[left][right] = Integer.max(dp[left][right], solve(left+1, right+1));
        }
        if (left < N && right < N && leftCards[left] > rightCards[right]) {
            dp[left][right] = Integer.max(dp[left][right], solve(left, right+1) + rightCards[right]);
        }
        return dp[left][right];
    }
}
