import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static int[][] matrix;

    private static int H, W;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());
        for (int t = 0; t < T; t++) {
            StringTokenizer st;
            st = new StringTokenizer(br.readLine().trim());
            int K = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());

            HashMap<Character, Integer> battleships = new HashMap();
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine().trim());
                battleships.put(st.nextToken().charAt(0), Integer.parseInt(st.nextToken()));
            }

            char[][] ipt = new char[H][W];
            for (int i = 0; i < H; i++) ipt[i] = br.readLine().trim().toCharArray();

            matrix = new int[H][W];
            int sy = 0, sx = 0;
            for (int y = 0; y < H; y++) {
                for (int x = 0; x < W; x++) {
                    if (ipt[y][x] == 'E') {
                        sy = y;
                        sx = x;
                    } else {
                        matrix[y][x] = battleships.get(ipt[y][x]);
                    }
                }
            }

            int[][] dist = new int[H][W];
            for (int i = 0; i < H; i++) Arrays.fill(dist[i], INF);

            PriorityQueue<Point> heap = new PriorityQueue();
            heap.add(new Point(sy, sx, 0));
            System.out.println(dijkstra(heap, dist));
        }

        br.close();
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < H && 0 <= x && x < W);
    }

    private static int dijkstra(PriorityQueue<Point> heap, int[][] dist) {
        dist[heap.peek().y][heap.peek().x] = 0;
        while (!heap.isEmpty()) {
            Point curr = heap.remove();
            if (dist[curr.y][curr.x] < curr.dist) continue;
            if (curr.y == H-1 || curr.y == 0 || curr.x == W-1 || curr.x == 0) return dist[curr.y][curr.x];

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx)) continue;
                if (dist[ny][nx] <= curr.dist + matrix[ny][nx]) continue;
                dist[ny][nx] = curr.dist + matrix[ny][nx];
                heap.add(new Point(ny, nx, dist[ny][nx]));
            }
        }
        return -1;
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
