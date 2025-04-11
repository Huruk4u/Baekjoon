import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken()), T = Integer.parseInt(st.nextToken());

        List<Node> nodes = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int s = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken()), x = Integer.parseInt(st.nextToken());
            nodes.add(new Node(s, y, x));
        }

        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) dist[i][i] = 0;

        for (int u = 0; u < N-1; u++) {
            for (int v = u + 1; v < N; v++) {
                dist[u][v] = getDistance(nodes.get(u), nodes.get(v));
                dist[v][u] = getDistance(nodes.get(v), nodes.get(u));

                if (nodes.get(u).special == 1 && nodes.get(v).special == 1) {
                    dist[u][v] = Math.min(dist[u][v], T);
                    dist[v][u] = Math.min(dist[v][u], T);
                }
            }
        }

        for (int k = 0; k < N; k++) {
            for (int u = 0; u < N; u++) {
                for (int v = 0; v < N; v++) {
                    dist[u][v] = Math.min(dist[u][v], dist[u][k] + dist[k][v]);
                }
            }
        }

        int M = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken()), v = Integer.parseInt(st.nextToken());
            System.out.println(dist[u-1][v-1]);
        }
        br.close();
    }

    private static class Node {
        int special, y, x;
        public Node(int special, int y, int x) {
            this.special = special;
            this.y = y;
            this.x = x;
        }
    }

    private static int getDistance(Node node1, Node node2) {
        return Math.abs(node1.y - node2.y) + Math.abs(node1.x - node2.x);
    }
}
