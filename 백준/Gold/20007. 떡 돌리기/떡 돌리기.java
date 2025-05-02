import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static List<Node>[] graph;

    public static int[] dist;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        ///////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) graph[i] = new ArrayList();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Node(v, w));
            graph[v].add(new Node(u, w));
        }
        ///////////////////////////// input

        dist = new int[N];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[Y] = 0;

        PriorityQueue<Node> heap = new PriorityQueue();
        heap.add(new Node(Y, 0));

        dijkstra(heap);
        Arrays.sort(dist);

        if (dist[N-1] > X) System.out.println(-1);
        else {
            int answer = 1;
            int temp = 0;
            for (int i = 0; i < N; i++) {
                if (temp + dist[i] * 2 > X) {
                    temp = dist[i] * 2;
                    answer++;
                } else {
                    temp += dist[i] * 2;
                }
            }
            System.out.println(answer);
        }

        br.close();
    }
    private static void dijkstra(PriorityQueue<Node> heap) {
        while (!heap.isEmpty()) {
            Node curr = heap.remove();
            if (dist[curr.number] < curr.dist) continue;

            for (Node next : graph[curr.number]) {
                if (dist[next.number] <= curr.dist + next.dist) continue;
                dist[next.number] = curr.dist + next.dist;
                heap.add(new Node(next.number, dist[next.number]));
            }
        }
        return;
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
            return String.format("[%d, %d]", number, dist);
        }
    }
}
