import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M;

    private static List<Edge>[] graph;

    private static int[][] dp;

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            if (u >= v) continue;
            graph[u].add(new Edge(v, weight));
        }

        dp = new int[N+1][M+1];
        for (int i = 1; i < N+1; i++) Arrays.fill(dp[i], -INF);
        dp[1][1] = 0;

        for (int i = 1; i < M; i++) {
            for (int u = 1; u < N+1; u++) {
                if (dp[u][i] == -INF) continue;
                for (Edge next : graph[u]) {
                    dp[next.number][i+1] = Math.max(dp[next.number][i+1], dp[u][i] + next.weight);
                }
            }
        }

        int answer = 0;
        for (int i = 1; i < M+1; i++) answer = Math.max(answer, dp[N][i]);
        System.out.println(answer);

        br.close();
    }

    private static class Edge {
        int number, weight;

        public Edge(int number, int weight) {
            this.number = number;
            this.weight = weight;
        }
    }
}
