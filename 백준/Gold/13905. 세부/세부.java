import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, INF = 987654321;

    private static List<Edge>[] graph;

    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine().trim());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

        PriorityQueue<Edge> edges = new PriorityQueue();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            edges.add(new Edge(u, v, w));
        }

        while (!edges.isEmpty()) {
            Edge edge = edges.remove();
            if (union(edge.curr, edge.next)) {
                graph[edge.curr].add(new Edge(edge.curr, edge.next, edge.weight));
                graph[edge.next].add(new Edge(edge.next, edge.curr, edge.weight));
            }
        }

        Queue<State> queue = new ArrayDeque();
        queue.add(new State(s, INF));
        System.out.println(bfs(queue, e));

        br.close();
    }

    private static int bfs(Queue<State> queue, int e) {
        boolean[] visited = new boolean[N+1];
        visited[queue.peek().number] = true;

        while (!queue.isEmpty()) {
            State curr = queue.remove();
            if (curr.number == e) return curr.minWeight;

            for (Edge edge : graph[curr.number]) {
                if (visited[edge.next]) continue;
                visited[edge.next] = true;
                queue.add(new State(edge.next, Integer.min(curr.minWeight, edge.weight)));
            }
        }
        return 0;
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static boolean union(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);

        if (root_u == root_v) return false;

        if (root_u < root_v) parent[root_v] = root_u;
        else parent[root_u] = root_v;
        return true;
    }

    private static class State {
        int number, minWeight;

        State(int number, int minWeight) {
            this.number = number;
            this.minWeight = minWeight;
        }
    }

    private static class Edge implements Comparable<Edge>{
        int curr, next, weight;

        Edge (int curr, int next, int weight) {
            this.curr = curr;
            this.next = next;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return -Integer.compare(this.weight, other.weight);
        }
    }
}
