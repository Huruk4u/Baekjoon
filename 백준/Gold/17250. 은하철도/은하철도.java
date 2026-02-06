import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int[] parent;

    private static long[] planets;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;

        planets = new long[N+1];
        for (int i = 1; i < N+1; i++) planets[i] = Long.parseLong(br.readLine().trim());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            System.out.println(union(u, v));
        }
        br.close();
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static long union(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);

        if (root_u == root_v) return planets[root_u];

        if (root_u < root_v) {
            parent[root_v] = root_u;
            planets[root_u] += planets[root_v];
            return planets[root_u];
        } else {
            parent[root_u] = root_v;
            planets[root_v] += planets[root_u];
            return planets[root_v];
        }
    }
}
