import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, Y;

    private static List<Node>[] graph;

    private static Long INF = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;


        //////////////////////////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Node(v, w));
        }
        st = new StringTokenizer(br.readLine().trim());
        int X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());
        int Z = Integer.parseInt(st.nextToken());
        //////////////////////////////////////////////// input

        PriorityQueue<Node> heap = new PriorityQueue<>();
        heap.add(new Node(X, 0));
        long[] useY = new long[N+1];
        Arrays.fill(useY, INF);
        dijkstra(heap, true, useY);


        heap = new PriorityQueue<>();
        heap.add(new Node(X, 0));
        long[] notUseY = new long[N+1];
        Arrays.fill(notUseY, INF);
        dijkstra(heap, false, notUseY);

        heap = new PriorityQueue<>();
        heap.add(new Node(Y, 0));
        long[] startY = new long[N+1];
        Arrays.fill(startY, INF);
        dijkstra(heap, false, startY);

        long rtn1 = (useY[Y] == INF || startY[Z] == INF)? -1: useY[Y] + startY[Z];
        long rtn2 = (notUseY[Z] == INF)? -1 : notUseY[Z];

        System.out.println(String.format("%d %d", rtn1, rtn2));

        br.close();
    }

    private static void dijkstra(PriorityQueue<Node> heap, boolean useY, long[] dist) {
        dist[heap.peek().number] = 0;
        while(!heap.isEmpty()) {
            Node curr = heap.remove();

            if (curr.weight > dist[curr.number]) continue;

            for (Node next : graph[curr.number]) {
                if (dist[next.number] <= dist[curr.number] + next.weight) continue;
                if (!useY && next.number == Y) continue;
                dist[next.number] = dist[curr.number] + next.weight;
                heap.add(new Node(next.number, dist[next.number]));
            }
        }
    }


    private static class Node implements Comparable<Node> {
        int number;
        long weight;
        Node(int number, long weight) {
            this.number = number;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node other) {
            return Long.compare(this.weight, other.weight);
        }

        @Override
        public String toString() {
            return "(" + this.number + " " + this.weight + ")";
        }
    }
}
