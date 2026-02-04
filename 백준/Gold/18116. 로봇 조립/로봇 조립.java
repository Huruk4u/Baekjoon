import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int[] parent, unionSize;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        parent = new int[1000001];
        for (int i = 1; i < 1000001; i++) parent[i] = i;

        unionSize = new int[1000001];
        Arrays.fill(unionSize, 1);

        int N = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            char token = st.nextToken().charAt(0);
            if (token == 'I') {
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                union(u, v);
            } else {
                int u = Integer.parseInt(st.nextToken());
                System.out.println(unionSize[find(u)]);
            }
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
            unionSize[root_u] += unionSize[root_v];
            parent[root_v] = root_u;
        } else {
            unionSize[root_v] += unionSize[root_u];
            parent[root_u] = root_v;
        }
    }
}
