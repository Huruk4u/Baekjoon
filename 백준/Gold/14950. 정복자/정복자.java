import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M, T;

    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        for (int i = 0; i < N+1; i++) parent[i] = i;

        PriorityQueue<Edge> heap = new PriorityQueue<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            heap.add(new Edge(u, v, w));
        }

        int answer = 0;
        while (!heap.isEmpty()) {
            Edge curr = heap.remove();
            if (union(curr.u, curr.v)) answer += curr.weight;
        }
        answer += T * (((N-1) * (N-2)) / 2);
        System.out.println(answer);

        br.close();
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static boolean union(int u, int v){
        int root_u = find(u);
        int root_v = find(v);

        if (root_u == root_v) return false;

        if (root_u < root_v) parent[root_v] = root_u;
        else parent[root_u] = root_v;
        return true;
    }

    private static class Edge implements Comparable<Edge> {
        int u, v, weight;

        Edge (int u, int v, int weight) {
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
