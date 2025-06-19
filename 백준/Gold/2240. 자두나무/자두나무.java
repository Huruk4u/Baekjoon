import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //////////////////////////////////////// input
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        int T = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[] drop = new int[T+1];
        for (int i = 1; i <= T; i++) drop[i] = Integer.parseInt(br.readLine().trim());
        //////////////////////////////////////// input
        int[][] dp = new int[T+1][W+1];
        for (int t = 1; t <= T; t++) {

            if (drop[t] == 1) dp[t][0] = dp[t-1][0] + 1;
            else dp[t][0] = dp[t-1][0];

            for (int jump = 1; jump <= W; jump++) {
                if (jump % 2 == 0) {
                    if (drop[t] == 1) dp[t][jump] = Integer.max(dp[t-1][jump] + 1, dp[t-1][jump-1]);
                    else dp[t][jump] = Integer.max(dp[t-1][jump], dp[t-1][jump-1] + 1);
                } else {
                    if (drop[t] == 1) dp[t][jump] = Integer.max(dp[t-1][jump], dp[t-1][jump-1] + 1);
                    else dp[t][jump] = Integer.max(dp[t-1][jump] + 1, dp[t-1][jump-1]);
                }
            }
        }

        int answer = 0;
        for (int i = 0; i <= W; i++) answer = Integer.max(answer, dp[T][i]);
        System.out.println(answer);

        br.close();
    }
}
