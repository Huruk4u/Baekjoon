import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<Node>[] graph;

    private static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        Queue<Node> queue = new ArrayDeque();
        List<Node> nodes = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            nodes.add(new Node(i, x, y));
            if (getDistance(x, y, X, Y) <= R) queue.add(nodes.get(i));
        }

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) graph[i] = new ArrayList();

        for (int u = 0; u < N; u++) {
            for (int v = u + 1; v < N; v++) {
                if (u == v) continue;
                if (getDistance(nodes.get(u).x, nodes.get(u).y, nodes.get(v).x, nodes.get(v).y) <= R) {
                    graph[u].add(nodes.get(v));
                    graph[v].add(nodes.get(u));
                }
            }
        }

        dist = new int[N];
        Arrays.fill(dist, -1);
        bfs(queue);

        double answer = 0;
        for (int i = 0; i < N; i++) {
            if (dist[i] == -1) continue;
            answer += D * Math.pow(0.5, dist[i]);
        }

        System.out.println(answer);

        br.close();
    }
    private static void bfs(Queue<Node> queue) {
        for (Node node : queue) dist[node.number] = 0;
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            for (Node next : graph[curr.number]) {
                if (dist[next.number] != -1) continue;
                dist[next.number] = dist[curr.number] + 1;
                queue.add(next);
            }
        }
    }

    private static class Node {
        int number, x, y;

        Node(int number, int x, int y) {
            this.number = number;
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    private static Double getDistance(int x1, int y1, int x2, int y2) {
        return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
    }
}
