import javax.print.DocFlavor;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int[][][] dp;

    private static char[] string;

    private static char[][] bridge;

    private static int BRIDGE_LENGTH, STRING_LENGTH;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        string = br.readLine().toCharArray();
        STRING_LENGTH = string.length;

        String devilBridge = br.readLine().trim();
        String angelBridge = br.readLine().trim();

        bridge = new char[2][devilBridge.length()];
        bridge[0] = devilBridge.toCharArray();
        bridge[1] = angelBridge.toCharArray();
        BRIDGE_LENGTH = bridge[0].length;

        // dp[현재 다리][다리의 위치][완성해야 하는 string 번호] : 끝까지 도달할 수 있는 가짓 수
        dp = new int[2][BRIDGE_LENGTH][STRING_LENGTH]; // 2 * 6 * 3
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < bridge[i].length; j++) Arrays.fill(dp[i][j], -1);
        }

        int answer = 0;
        for (int currBridge = 0; currBridge < 2; currBridge++) {
            for (int bridgeIdx = 0; bridgeIdx < BRIDGE_LENGTH; bridgeIdx++) {
                if (string[0] == bridge[currBridge][bridgeIdx]) answer += solve(currBridge, bridgeIdx, 1);
            }
        }

        System.out.println(answer);

        br.close();
    }

    private static int solve(int currBridge, int bridgeIdx, int stringIdx) {
        if (stringIdx == STRING_LENGTH) return 1; // 모든 문자열이 완성되었으면 가짓수 1을 반환한다.
        if (bridgeIdx == BRIDGE_LENGTH) return 0; // 문자열이 완성되지 않았는데, 다리의 끝에 도달했으면 가짓수 0을 반환한다.
        if (dp[currBridge][bridgeIdx][stringIdx] != -1) return dp[currBridge][bridgeIdx][stringIdx]; // 메모아이제이션

        dp[currBridge][bridgeIdx][stringIdx] = 0;

        for (int i = bridgeIdx + 1; i < BRIDGE_LENGTH; i++) {
            if (currBridge == 0) { // 0번 bridge에 있다면,
                if (string[stringIdx] == bridge[1][i]) dp[currBridge][bridgeIdx][stringIdx] += solve(1, i, stringIdx+1);
            } else { // 1번 bridge에 있다면,
                if (string[stringIdx] == bridge[0][i]) dp[currBridge][bridgeIdx][stringIdx] += solve(0, i, stringIdx+1);
            }
        }

        return dp[currBridge][bridgeIdx][stringIdx];
    }
}
