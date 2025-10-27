import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static List<Integer>[] graph;

    private static int[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine().trim());
        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();
        for (int curr = 1; curr < N+1; curr++) {
            int parent = Integer.parseInt(st.nextToken());
            if (parent == -1) continue;

            graph[parent].add(curr);
        }

        dp = new int[N+1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int node = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            dp[node] += weight;
        }

        dfs(1, dp[1]);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N+1; i++) sb.append(dp[i]).append(" ");
        System.out.println(sb.toString().trim());

        br.close();
    }

    private static void dfs(int curr, int weight) {
        dp[curr] += weight;
        for (int next: graph[curr]) dfs(next, dp[curr]);
    }
}
