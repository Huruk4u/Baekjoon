import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int[] parent;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;

        long initCost = 0;
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            initCost += w;
            edges.add(new Edge(u, v, w));
        }

        long buildCost = 0;
        Collections.sort(edges);
        for (Edge edge : edges) {
            if (union(edge)) buildCost += edge.weight;
        }

        long answer = initCost - buildCost;
        for (int i = 1; i < N+1; i++) {
            if (find(i) != 1) {
                answer = -1;
                break;
            }
        }
        System.out.println(answer);


        br.close();
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static boolean union(Edge edge) {
        int root_u = find(edge.u);
        int root_v = find(edge.v);

        if (root_u == root_v) return false;

        if (root_u < root_v) parent[root_v] = root_u;
        else parent[root_u] = root_v;

        return true;

    }

    private static class Edge implements Comparable<Edge> {
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
    }
}
