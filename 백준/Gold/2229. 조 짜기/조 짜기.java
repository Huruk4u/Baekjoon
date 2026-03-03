import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine().trim());

        st = new StringTokenizer(br.readLine().trim());
        int[] A = new int[N+1];
        for (int i = 1; i < N+1; i++) A[i] = Integer.parseInt(st.nextToken());

        int[] dp = new int[N+1];

        for (int i = 1; i < N+1; i++) {
            int max = A[i];
            int min = A[i];
            for (int j = i; j >= 1; j--) {
                max = Integer.max(max, A[j]);
                min = Integer.min(min, A[j]);
                dp[i] = Integer.max(dp[i], max - min + dp[j-1]);
            }
        }
        System.out.println(dp[N]);
    }
}
