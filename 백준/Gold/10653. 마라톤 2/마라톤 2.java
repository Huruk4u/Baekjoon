import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N, K;

    private static int[][][] dp;

    private static Node[] nodes;

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            nodes[i] = new Node(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        dp = new int[N][N][K+1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) Arrays.fill(dp[i][j], INF);
        };

        System.out.println(dfs(0, 0, 0));

        br.close();
    }

    private static int dfs(int curr, int prev, int k) {
        if (curr == N-1) return getDistance(nodes[curr], nodes[prev]);
        if (dp[curr][prev][k] != INF) return dp[curr][prev][k];

        dp[curr][prev][k] = dfs(curr+1, curr, k) + getDistance(nodes[curr], nodes[prev]);
        if (k < K && curr < N-1) {
            dp[curr][prev][k] = Math.min(dp[curr][prev][k], dfs(curr+1, prev, k+1));
        }

        return dp[curr][prev][k];
    }

    private static int getDistance(Node node1, Node node2) {
        return Math.abs(node1.x - node2.x) + Math.abs(node1.y - node2.y);
    }

    private static class Node {
        int x, y;

        private Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
