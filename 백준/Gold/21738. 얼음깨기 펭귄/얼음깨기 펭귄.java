import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, S, P;

    private static List<Integer>[] graph;

    private static int[] prev;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        prev = new int[N+1];
        Queue<Integer> queue = new ArrayDeque();
        queue.add(P);

        int[] rtn = bfs(queue);
        TreeSet<Integer> path = new TreeSet();

        int curr = rtn[0];
        while (curr != P) {
            path.add(curr);
            curr = prev[curr];
        }
        curr = rtn[1];
        while (curr != P) {
            path.add(curr);
            curr= prev[curr];
        }
        System.out.println(N - path.size() - 1);

        br.close();
    }

    private static int[] bfs(Queue<Integer> queue) {
        boolean[] visited = new boolean[N+1];
        visited[P] = true;
        int cnt = 0;
        int[] rtn = {0, 0};

        while (!queue.isEmpty()) {
            int curr = queue.remove();
            if (curr <= S) {
                rtn[cnt] = curr;
                cnt++;
            }
            if (cnt == 2) return rtn;

            for (int next: graph[curr]) {
                if (visited[next]) continue;
                visited[next] = true;
                prev[next] = curr;
                queue.add(next);
            }
        }
        return rtn;
    }
}
