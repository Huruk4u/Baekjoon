import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;

    private static double M;

    private static double[][] weight;

    private static double[] dist;

    private static Double INF = 987654321.0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[][] points = new int[N+1][2];
        M = Double.parseDouble(br.readLine().trim());
        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
        }

        weight = new double[N+1][N+1];
        for (int u = 1; u < N+1; u++) {
            for (int v = 1; v < N+1; v++) {
                weight[u][v] = getDistance(points[u], points[v]);
            }
        }
        for (int i = 0; i < W; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            weight[u][v] = 0;
            weight[v][u] = 0;
        }

        PriorityQueue<Point> heap = new PriorityQueue();
        heap.add(new Point(1, 0));

        dist = new double[N+1];
        Arrays.fill(dist, INF);

        System.out.println((int) (dijkstra(heap) * 1000));

        br.close();
    }

    private static double dijkstra(PriorityQueue<Point> heap) {
        dist[heap.peek().number] = 0;
        while (!heap.isEmpty()) {
            Point curr = heap.remove();
            if (dist[curr.number] < curr.dist) continue;
            if (curr.number == N) return dist[curr.number];

            for (int next = 1; next < N+1; next++) {
                if (curr.number == next || weight[curr.number][next] > M) continue;
                if (dist[next] <= curr.dist + weight[curr.number][next]) continue;

                dist[next] = curr.dist + weight[curr.number][next];
                heap.add(new Point(next, dist[next]));
            }
        }
        return -1;
    }

    private static double getDistance(int[] node1, int[] node2) {
        return Math.sqrt(Math.pow(node1[0] - node2[0], 2) + Math.pow(node1[1] - node2[1], 2));
    }


    private static class Point implements Comparable<Point> {
        int number;
        double dist;

        public Point(int number) {
            this.number = number;
        }

        public Point(int number, double dist) {
            this.number = number;
            this.dist = dist;
        }

        @Override
        public int compareTo(Point other) {
            return Double.compare(this.dist, other.dist);
        }
    }
}
