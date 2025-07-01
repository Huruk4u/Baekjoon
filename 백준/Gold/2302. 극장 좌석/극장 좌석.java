import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ///////////////////////////////// input
        int N = Integer.parseInt(br.readLine().trim());

        int M = Integer.parseInt(br.readLine().trim());
        boolean[] vip = new boolean[N+1];
        for (int i = 0; i < M; i++) vip[Integer.parseInt(br.readLine().trim())] = true;
        ///////////////////////////////// input
        int[] dp = new int[41];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < 41; i++) dp[i] = dp[i - 1] + dp[i - 2];

        int answer = 1;
        int temp = 0;
        for (int i = 1; i < N+1; i++) {
            if (!vip[i]) {
                temp++;
            } else {
                if (temp != 0) answer *= dp[temp];
                temp = 0;
            }
        }
        if (temp != 0) answer *= dp[temp];

        System.out.println(answer);

        br.close();
    }
}
