import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<Edge>[] graph;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int V = Integer.parseInt(st.nextToken()), E = Integer.parseInt(st.nextToken()), P = Integer.parseInt(st.nextToken());

        graph = new ArrayList[V+1];
        for (int i = 0; i < V+1; i++) graph[i] = new ArrayList<>();
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));
        }

        /**
         * 민준에서 다른 도착지까지 가는 경로
         */
        int[] distMinjun = new int[V+1];
        Arrays.fill(distMinjun, 987654321);

        PriorityQueue<Node> heap = new PriorityQueue<>();
        heap.add(new Node(1, 0));

        dijkstra(heap, distMinjun);
//        System.out.println(Arrays.toString(distMinjun));

        /**
         * 건우에서 다른 도착지까지 가는 경로
         */
        int[] distKeonwoo = new int[V+1];
        Arrays.fill(distKeonwoo, 987654321);

        heap.clear();
        heap.add(new Node(P, 0));

        dijkstra(heap, distKeonwoo);
//        System.out.println(Arrays.toString(distKeonwoo));

        String answer = (distMinjun[V] == distMinjun[P] + distKeonwoo[V])? "SAVE HIM" : "GOOD BYE";
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
        Edge (int next, int weight) {
            this.number = next;
            this.weight = weight;
        }
    }

    private static class Node implements Comparable<Node> {
        int number, dist;
        Node (int number, int dist) {
            this.number = number;
            this.dist = dist;
        }
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.dist, other.dist);
        }
    }

}
