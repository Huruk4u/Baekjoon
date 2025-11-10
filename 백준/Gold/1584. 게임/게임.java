import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static int[][] matrix, visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        matrix = new int[501][501];

        int N = Integer.parseInt(br.readLine().trim());
        for (int i = 0;  i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int y1 = Integer.parseInt(st.nextToken());
            int x1 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            int sy = Integer.min(y1, y2);
            int ey = Integer.max(y1, y2);
            int sx = Integer.min(x1, x2);
            int ex = Integer.max(x1, x2);

            for (int y = sy; y <= ey; y++) {
                for (int x = sx; x <= ex; x++) {
                    matrix[y][x] = 1;
                }
            }
        }

        int M = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int y1 = Integer.parseInt(st.nextToken());
            int x1 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            int sy = Integer.min(y1, y2);
            int ey = Integer.max(y1, y2);
            int sx = Integer.min(x1, x2);
            int ex = Integer.max(x1, x2);

            for (int y = sy; y <= ey; y++) {
                for (int x = sx; x <= ex; x++) {
                    matrix[y][x] = 2;
                }
            }
        }

        PriorityQueue<Node> heap = new PriorityQueue<>();
        heap.add(new Node(0, 0, 0));

        visited = new int[501][501];
        for (int i = 0; i < 501; i++) Arrays.fill(visited[i], INF);
        visited[0][0] = 0;
        
        System.out.println(dijkstra(heap));

        br.close();
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < 501 && 0 <= x && x < 501);
    }

    private static int dijkstra(PriorityQueue<Node> heap) {
        while (!heap.isEmpty()) {
            Node curr = heap.remove();
            if (visited[curr.y][curr.x] < curr.cost) continue;
            if (curr.y == 500 && curr.x == 500) return visited[curr.y][curr.x];

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx) || matrix[ny][nx] == 2) continue;

                int weight = (matrix[ny][nx] == 1)? 1 : 0;
                if (visited[ny][nx] <= curr.cost + weight) continue;

                visited[ny][nx] = visited[curr.y][curr.x] + weight;
                heap.add(new Node(ny, nx, visited[ny][nx]));
            }
        }
        return -1;
    }

    private static class Node implements Comparable<Node> {
        int y, x, cost;
        public Node(int y, int x, int cost) {
            this.y = y;
            this.x = x;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
}
