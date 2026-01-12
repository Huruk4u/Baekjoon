import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, Q;

    private static List<Edge>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            Queue<Integer> queue = new ArrayDeque();
            queue.add(v);

            System.out.println(bfs(queue, k));
        }


        br.close();
    }

    private static int bfs(Queue<Integer> queue, int k) {
        boolean[] visited = new boolean[N+1];
        visited[queue.peek()] = true;

        int rtn = 0;
        while (!queue.isEmpty()) {
            Integer curr = queue.remove();
            rtn++;
            for (Edge next : graph[curr]) {
                if (visited[next.number] || next.weight < k) continue;

                visited[next.number] = true;
                queue.add(next.number);
            }
        }
        return rtn-1;
    }

    private static class Edge {
        int number, weight;
        public Edge(int number, int weight) {
            this.number = number;
            this.weight = weight;
        }
    }
}
