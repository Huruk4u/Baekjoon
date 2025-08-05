import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

    private static int[][] matrix;

    private static boolean[][] visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    private static int[] parent;

    private static int N, M;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ipt = br.readLine().trim().split(" ");
        N = Integer.parseInt(ipt[0]);
        M = Integer.parseInt(ipt[1]);

        matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            ipt = br.readLine().trim().split("");
            for (int j = 0; j < M; j++) {
                if (ipt[j].equals("U")) matrix[i][j] = 0;
                else if (ipt[j].equals("D")) matrix[i][j] = 1;
                else if (ipt[j].equals("L")) matrix[i][j] = 2;
                else matrix[i][j] = 3;
            }
        }

        parent = new int[N * M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) parent[i * M + j] = i * M + j;
        }

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                dfs(y, x);
            }
        }

//        System.out.println(Arrays.toString(parent));
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < N * M; i++) set.add(find(i));
        System.out.println(set.size());

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

    private static void dfs(int cy, int cx) {
        int ny = cy + dy[matrix[cy][cx]];
        int nx = cx + dx[matrix[cy][cx]];

        if(union(cy * M + cx, ny * M + nx)) {
            dfs(ny, nx);
        } else return;
    }
}
