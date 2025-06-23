import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    private static long MOD = 1000000;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] code = br.readLine().trim().split("");

        if (code[0].equals("0")) {
            System.out.println(0);
            return;
        }

        ///////////////////////////// 초기값 설정
        long[] dp = new long[code.length + 1];
        dp[0] = 1;
        dp[1] = 1;
        ///////////////////////////// 초기값 설정
        for (int i = 2; i <= code.length; i++) {
            int codeWithNext = Integer.parseInt(code[i-2] + code[i-1]);
            if (code[i-1].equals("0")) {
                if (codeWithNext == 10 || codeWithNext == 20) dp[i] = dp[i - 2] % MOD;
                else break;
            } else {
                if (10 <= codeWithNext && codeWithNext <= 26) dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
                else dp[i] = dp[i - 1] % MOD;
            }
        }
        System.out.println(dp[code.length] % MOD);

        br.close();
    }
}
