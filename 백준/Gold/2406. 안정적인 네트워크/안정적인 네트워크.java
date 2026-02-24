import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        List<Edge> edges = new ArrayList<>();
        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            edges.add(new Edge(u, v, 0));
        }

        int[][] cost = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < N; j++) cost[i][j] = Integer.parseInt(st.nextToken());
        }

        parent = new int[N];
        for (int i = 0; i < N; i++) parent[i] = i;

        for (Edge edge : edges) {
            cost[edge.u-1][edge.v-1] = edge.weight;
            cost[edge.v-1][edge.u-1] = edge.weight;
            union(edge.u-1, edge.v-1);
        }


        edges = new ArrayList<>();
        for (int u = 1; u < N; u++) {
            for (int v = u+1; v < N; v++) {
                if (find(u) == find(v)) continue;
                edges.add(new Edge(u, v, cost[u][v]));
            }
        }
        edges.sort(Edge::compareTo);

        int X = 0, K = 0;
        List<Edge> answers = new ArrayList<>();
        for (Edge edge : edges) {
            if (union(edge.u, edge.v)) {
                X += edge.weight;
                K++;
                answers.add(edge);
            }
        }
        System.out.println(String.format("%d %d", X, K));
        for (Edge edge : answers) {
            System.out.println(String.format("%d %d", edge.u+1, edge.v+1));
        }

        br.close();
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

    private static class Edge implements Comparable<Edge>{
        int u, v, weight;

        Edge(int u, int v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.weight, other.weight);
        }

        @Override
        public String toString() {
            return String.format("(%d %d %d)", u, v, weight);
        }
    }
}
