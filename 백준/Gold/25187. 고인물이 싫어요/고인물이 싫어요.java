import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int[] parent;

    private static int[] pure;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        pure = new int[N+1];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 1; i < N+1; i++) {
            int k = Integer.parseInt(st.nextToken());
            if (k == 0) pure[i] = -1;
            else pure[i] = 1;
        }

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            union(u, v);
        }

        for (int i = 0; i < Q; i++) {
            int k = Integer.parseInt(br.readLine().trim());
            if (pure[find(k)] > 0) System.out.println(1);
            else System.out.println(0);
        }

        br.close();
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static void union(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);

        if (root_u == root_v) return;

        if (root_u < root_v) {
            parent[root_v] = root_u;
            pure[root_u] += pure[root_v];
        } else {
            parent[root_u] = root_v;
            pure[root_v] += pure[root_u];
        }
    }
}
