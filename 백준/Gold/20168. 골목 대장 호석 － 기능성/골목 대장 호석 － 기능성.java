import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M;

    private static List<Edge>[] graph;

    private static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine().trim());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));
        }
        dp = new int[N+1];
        Arrays.fill(dp, Integer.MAX_VALUE);

        PriorityQueue<Node> heap = new PriorityQueue();
        heap.add(new Node(A, 0));
        System.out.println(dijkstra(heap, A, B, C));

        br.close();
    }

    private static int dijkstra(PriorityQueue<Node> heap, int start, int target, int limitCost) {
        dp[start] = 0;
        while (!heap.isEmpty()) {
            Node curr = heap.remove();

            if (curr.number == target) return dp[curr.number];
            if (dp[curr.number] < curr.dist) continue;

            for (Edge next : graph[curr.number]) {
                if (curr.dist + next.weight > limitCost) continue;
                if (dp[next.number] <= Integer.max(dp[curr.number], next.weight)) continue;

                dp[next.number] = Integer.max(dp[curr.number], next.weight);
                heap.add(new Node(next.number, curr.dist + next.weight));
            }
        }
        return -1;
    }

    private static class Node implements Comparable<Node> {
        int number, dist;
        public Node(int number, int dist) {
            this.number = number;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.dist, other.dist);
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", number, dist);
        }
    }

    private static class Edge {
        int number, weight;
        public Edge(int number, int weight) {
            this.number = number;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", number, weight);
        }
    }
}
