import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );

        int N = Integer.parseInt(br.readLine());

        int[][] cost = new int[N][N];

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) cost[i][j] = Integer.parseInt(st.nextToken());
        }

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) edges.add(new Edge(i, j, cost[i][j]));
        }
        Collections.sort(edges);

        int[] parent = new int[N];
        for (int i = 0; i < N; i++) parent[i] = i;

        long answer = 0;
        for (Edge edge : edges) answer += union(edge, parent);

        System.out.println(answer);

        br.close();
    }

    private static void pprint(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) System.out.println(Arrays.toString(matrix[i]));
    }

    private static int find(int node, int[] parent) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node], parent);
        return parent[node];
    }

    private static int union(Edge edge, int[] parent) {
        int root_u = find(edge.u, parent);
        int root_v = find(edge.v, parent);
        if (root_u == root_v) return 0;

        if (root_u < root_v) parent[root_v] = root_u;
        else parent[root_u] = root_v;

        return edge.weight;
    }

    private static class Edge implements Comparable<Edge> {
        int u;
        int v;
        int weight;

        Edge (int u, int v, int weight) {
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
            return "Edge{" +
                    "u=" + u +
                    ", v=" + v +
                    ", weight=" + weight +
                    '}';
        }
    }
}
