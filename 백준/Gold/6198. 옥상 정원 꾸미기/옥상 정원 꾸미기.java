import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().trim());
        long[] A = new long[N];
        for (int i = 0; i < N; i++) A[i] = Long.parseLong(br.readLine().trim());

        int[] dp = new int[N];
        for (int i = N-1; i >= 0; i--) {
            int pivot = i;
            int temp = 1;
            while (pivot + temp < N) {
                if (A[pivot] <= A[pivot + temp]) break;
                dp[pivot] += dp[pivot + temp] + 1;
                temp += 1 + dp[pivot + temp];
            }
        }

        long answer = 0;
        for (int i = 0; i < N; i++) answer += dp[i];
        System.out.println(answer);

        br.close();
    }
}
