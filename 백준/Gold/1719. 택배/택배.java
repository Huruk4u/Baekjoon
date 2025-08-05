import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<Edge>[] graph;

    private static int[][] dist, startingPoint;

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u ,w));
        }

        dist = new int[N+1][N+1];
        startingPoint = new int[N+1][N+1];
        for (int i = 0; i < N+1; i++) Arrays.fill(dist[i], INF);

        for (int i = 1; i < N+1; i++) {
            PriorityQueue<Node> heap = new PriorityQueue();
            heap.add(new Node(i, 0));

            dist[i][i] = 0;
            dijkstra(heap, i);
        }

        for (int i = 1; i < N+1; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 1; j < N+1; j++) {
                if (i == j) sb.append("- ");
                else sb.append(startingPoint[i][j] + " ");
            }
            System.out.println(sb.toString().trim());
        }

        br.close();
    }

    private static void dijkstra(PriorityQueue<Node> heap, int startingNode) {
        while(!heap.isEmpty()) {
            Node curr = heap.remove();

            if (curr.cost > dist[startingNode][curr.number]) continue;
            if (startingPoint[startingNode][curr.number] == 0){
                startingPoint[startingNode][curr.number] = curr.starting;
            }

//            System.out.println(String.format("%d starting %d visited, %d initialNode", startingNode, curr.number, curr.starting));

            for (Edge next : graph[curr.number]) {
                if (dist[startingNode][next.number] <= curr.cost + next.weight) continue;

                dist[startingNode][next.number] = curr.cost + next.weight;

                Node nextNode = new Node(next.number, dist[startingNode][next.number]);
                if (curr.number == startingNode) nextNode.starting = next.number;
                else nextNode.starting = curr.starting;

                heap.add(nextNode);
            }
        }
    }

    private static class Node implements Comparable<Node> {
        int number, cost, starting;
        Node(int number, int cost) {
            this.number = number;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    private static class Edge {
        int number, weight;

        Edge(int next, int weight) {
            this.number = next;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", number, weight);
        }
    }
}
