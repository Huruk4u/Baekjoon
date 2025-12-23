import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        parent = new int[N + 1];
        for (int i = 1; i < N + 1; i++) parent[i] = i;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            union(u, v);
        }

        int[] order = new int[N];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) order[i] = Integer.parseInt(st.nextToken());

        int answer = 0;
        for (int i = 1; i < N; i++) {
            if (find(order[i-1]) != find(order[i])) answer++;
        }
        System.out.println(answer);

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

        if (root_u < root_v) parent[root_v] = root_u;
        else parent[root_u] = root_v;
        return;
    }
}
