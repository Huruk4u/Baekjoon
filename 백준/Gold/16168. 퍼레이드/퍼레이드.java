import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int V, E;

    private static List<Integer>[] graph;

    private static int[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList[V+1];
        for (int i = 1; i < V+1; i++) graph[i] = new ArrayList();

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        visited = new int[V+1][V+1];
        String answer = "NO";
        for (int i = 1; i < V+1; i++) {
            if (dfs(i, i, 0)) {
                answer = "YES";
                break;
            }
        }
        System.out.println(answer);
        br.close();
    }

    private static boolean dfs(int curr, int start, int depth) {
        if (depth == E) return true;

        boolean rtn = false;
        for (int next : graph[curr]) {
            if (visited[curr][next] == start || visited[next][curr] == start) continue;
            visited[curr][next] = start;
            visited[next][curr] = start;
            rtn |= dfs(next, start, depth+1);
        }

        return rtn;
    }
}
