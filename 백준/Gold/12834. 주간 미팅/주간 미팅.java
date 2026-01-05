import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<Edge>[] graph;

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine().trim());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int[] teams = new int[N];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) {
            teams[i] = Integer.parseInt(st.nextToken());
        }

        graph = new List[V+1];
        for (int i = 1; i < V+1; i++) graph[i] = new ArrayList();
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));
        }

        PriorityQueue<Node> heapKIST = new PriorityQueue();
        heapKIST.add(new Node(A, 0));

        int[] distKIST = new int[V+1];
        Arrays.fill(distKIST, INF);
        dijkstra(heapKIST, distKIST);

        PriorityQueue<Node> heapSEAL = new PriorityQueue();
        heapSEAL.add(new Node(B, 0));

        int[] distSEAL = new int[V+1];
        Arrays.fill(distSEAL, INF);
        dijkstra(heapSEAL, distSEAL);

        int answer = 0;
        for (int team : teams) {
            int dk = distKIST[team] == INF ? -1 : distKIST[team];
            int ds = distSEAL[team] == INF ? -1 : distSEAL[team];
            answer += (dk + ds);
        }
        System.out.println(answer);

        br.close();
    }

    private static void dijkstra(PriorityQueue<Node> heap, int[] dist) {
        dist[heap.peek().number] = 0;
        while (!heap.isEmpty()) {
            Node curr = heap.remove();
            if (dist[curr.number] < curr.dist) continue;

            for (Edge next : graph[curr.number]) {
                if (dist[next.number] <= curr.dist + next.weight) continue;
                dist[next.number] = curr.dist + next.weight;
                heap.add(new Node(next.number, dist[next.number]));
            }
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
    }
}
