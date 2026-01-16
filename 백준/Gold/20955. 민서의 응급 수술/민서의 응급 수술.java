import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

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

        int answer = 0;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            if (!union(u, v)) answer++;
        }

        for (int i = 1; i < N+1; i++) {
            if (union(i, 1)) answer++;
        }
        System.out.println(answer);

        br.close();
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static boolean union(int u, int v) {
        int node_u = find(u);
        int node_v = find(v);

        if (node_u == node_v) return false;

        if (node_u < node_v) parent[node_v] = node_u;
        else parent[node_u] = node_v;
        return true;
    }
}
