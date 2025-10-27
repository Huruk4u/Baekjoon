import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    private static List<Integer>[] graph;

    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());

            graph = new ArrayList[N+1];
            for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();
            for (int i = 0; i < N-1; i++) {
                st = new StringTokenizer(br.readLine().trim());
                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                graph[child].add(parent);
            }

            st = new StringTokenizer(br.readLine().trim());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());

            visited = new boolean[N+1];
            dfs(node1);
            int answer = dfs(node2);

            System.out.println(answer);
        }

        br.close();
    }

    private static int dfs(int curr) {
        if (visited[curr]) return curr;
        visited[curr] = true;

        int rtn = -1;
        for (int next : graph[curr]) rtn = Integer.max(rtn, dfs(next));

        return rtn;
    }
}
