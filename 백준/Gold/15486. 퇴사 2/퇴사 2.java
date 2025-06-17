import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    private static int[] dp, delay, price;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        ///////////////////////////////////// input
        N = Integer.parseInt(br.readLine());
        delay = new int[N];
        price = new int[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());

            delay[i] = Integer.parseInt(st.nextToken());
            price[i] = Integer.parseInt(st.nextToken());
        }
        ///////////////////////////////////// input

        dp = new int[N];
        Arrays.fill(dp, -1);

        System.out.println(solve(0));

        br.close();
    }

    private static int solve(int idx) {
        if (idx >= N) return 0;
        if (dp[idx] != -1) return dp[idx];

        if (idx + delay[idx] <= N)  dp[idx] = Integer.max(solve(idx + 1), solve(idx + delay[idx]) + price[idx]);
        else dp[idx] = solve(idx + 1);

        return dp[idx];
    }
}
