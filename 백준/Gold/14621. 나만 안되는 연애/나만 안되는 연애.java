import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    private static int[] parent;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        ////////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String[] iptColor = br.readLine().trim().split(" ");
        boolean[] color = new boolean[N+1];
        for (int i = 1; i < N+1; i++) color[i] = iptColor[i-1].equals("M");

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            edges.add(new Edge(u, v, w));
        }
        Collections.sort(edges);
        ////////////////////////////// input

        parent = new int[N + 1];
        for (int i = 1; i < N+1; i++) parent[i] = i;

        int answer = 0;
        for (Edge edge : edges) {
            if (color[edge.x] == color[edge.y]) continue;
            answer += union(edge);
        }

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

    private static int union(Edge edge) {
        int root_x = find(edge.x);
        int root_y = find(edge.y);
        if (root_x == root_y) return 0;

        if (root_x < root_y) parent[root_y] = root_x;
        else parent[root_x] = root_y;
        return edge.weight;
    }

    private static class Edge implements Comparable<Edge> {
        int x, y, weight;
        Edge(int x, int y, int weight) {
            this.x = x;
            this.y = y;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.weight, other.weight);
        }
    }
}
