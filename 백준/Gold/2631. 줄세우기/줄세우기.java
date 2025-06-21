import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ////////////////////////////////// input
        int N = Integer.parseInt(br.readLine().trim());

        int[] A = new int[N];
        for (int i = 0; i < N; i++) A[i] = Integer.parseInt(br.readLine().trim());
        ////////////////////////////////// input

        int[] dp = new int[N];
        Arrays.fill(dp, 1);

        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                if (A[i] >= A[j]) continue;
                dp[j] = Integer.max(dp[j], dp[i] + 1);
            }
        }

        int maxLength = 0;
        for (int i = 0; i < N; i++) maxLength = Integer.max(maxLength, dp[i]);

        System.out.println(N - maxLength);

        br.close();
    }
}
