import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static boolean[][][][][] dp;

    private static String answer;

    public static void main(String[] args) throws IOException {

        //////////////////////////////////////////////// input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] ipt = br.readLine().trim().toCharArray();
        int A = 0, B = 0, C = 0;
        for (char c : ipt) {
            if (c == 'A') A++;
            else if (c == 'B') B++;
            else C++;
        }
        //////////////////////////////////////////////// input

        dp = new boolean[A+1][B+1][C+1][3][3];

        dfs(A, B, C, "", 0, 0);
        if (answer == null) System.out.println(-1);
        else System.out.println(answer);

        br.close();
    }

    private static void dfs(int a, int b, int c, String sequence, int prev2, int prev1) {
        if(a == 0 && b == 0 && c == 0) {
            answer = sequence;
            return;
        }
        if (answer != null) return;
        if(dp[a][b][c][prev2][prev1]) return;

        dp[a][b][c][prev2][prev1] = true;

        if (a > 0) dfs(a - 1, b, c, sequence + "A", prev1, 0);
        if (b > 0 && prev1 != 1) dfs(a, b - 1, c, sequence + "B", prev1, 1);
        if (c > 0 && prev1 != 2 && prev2 != 2) dfs(a, b, c - 1, sequence + "C", prev2, 2);
    }
}
