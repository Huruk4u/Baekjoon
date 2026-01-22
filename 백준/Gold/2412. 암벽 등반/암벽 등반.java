import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int T;

    private static HashMap<Node, List<Node>> graph;

    private static HashMap<Node, Integer> dist = new HashMap();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        graph = new HashMap();
        dist = new HashMap();

        graph.put(new Node(0, 0), new ArrayList());
        dist.put(new Node(0, 0), 0);
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph.put(new Node(x, y), new ArrayList());
            dist.put(new Node(x, y), -1);
        }

        for (Node node : graph.keySet()) {
            for (int dx = -2; dx <= 2; dx++) {
                for (int dy = -2; dy <= 2; dy++) {
                    if (dx == 0 && dy == 0) continue;
                    Node next = new Node(node.x + dx, node.y + dy);
                    if (!graph.containsKey(next)) continue;
                    graph.get(node).add(next);
                }
            }
        }

        Queue<Node> queue = new ArrayDeque();
        queue.add(new Node(0, 0));
        System.out.println(bfs(queue));

        br.close();
    }

    private static int bfs(Queue<Node> queue) {
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            if (curr.y == T) return dist.get(curr);

            for (Node next : graph.get(curr)) {
                if (dist.get(next) != -1) continue;
                dist.replace(next, dist.get(curr) + 1);
                queue.add(next);
            }
        }
        return -1;
    }

    private static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object other) {
            if (this == other) return true;
            if (other == null || getClass() != other.getClass()) return false;
            Node node = (Node) other;
            return x == node.x && y == node.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}
