import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;

    private static int[][] matrix;

    private static int[][] dist;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine().trim());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < M; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }

        if (matrix[0][0] == -1) {
            System.out.println(-1);
        } else {
            dist = new int[N][M];
            for (int i = 0; i < N; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);

            PriorityQueue<Point> heap = new PriorityQueue();
            heap.add(new Point(0, 0, matrix[0][0]));

            System.out.println(dijkstra(heap));
        }

        br.close();
    }

    private static int dijkstra(PriorityQueue<Point> heap) {
        dist[heap.peek().y][heap.peek().x] = matrix[heap.peek().y][heap.peek().x];
        while (!heap.isEmpty()) {
            Point curr = heap.remove();
            if (curr.y == N-1 && curr.x == M-1) return dist[curr.y][curr.x];
            if (dist[curr.y][curr.x] < curr.dist) continue;

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                if (!inRange(ny, nx) || matrix[ny][nx] == -1) continue;
                if (dist[ny][nx] <= curr.dist + matrix[ny][nx]) continue;

                dist[ny][nx] = curr.dist + matrix[ny][nx];
                heap.add(new Point(ny, nx, dist[ny][nx]));
            }
        }
        return -1;
    }


    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < M);
    }

    private static class Point implements Comparable<Point> {
        int y, x, dist;

        public Point(int y, int x, int dist) {
            this.y = y;
            this.x = x;
            this.dist = dist;
        }

        @Override
        public int compareTo(Point other) {
            return Integer.compare(this.dist, other.dist);
        }
    }
}
