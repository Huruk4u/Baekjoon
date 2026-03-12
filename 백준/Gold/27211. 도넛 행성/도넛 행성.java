import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;

    private static int[][] matrix, visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        matrix = new int[N][M];
        visited = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (visited[y][x] == 1 || matrix[y][x] == 1) continue;
                Queue<Point> queue = new ArrayDeque<>();
                queue.add(new Point(y, x));
                visited[y][x] = 1;
                bfs(queue);
                answer++;
            }
        }
        System.out.println(answer);

        br.close();
    }
    private static void bfs(Queue<Point> queue) {
        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                if (!inRange(ny, nx)) {
                    if (ny < 0) ny = N-1;
                    if (ny >= N) ny = 0;
                    if (nx < 0) nx = M-1;
                    if (nx >= M) nx = 0;
                }
                if (matrix[ny][nx] == 1 || visited[ny][nx] == 1) continue;
                visited[ny][nx] = 1;
                queue.add(new Point(ny, nx));
            }
        }
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N) && (0 <= x && x < M);
    }

    private static class Point {
        int y, x;

        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public String toString() {
            return "(" + y + ", " + x + ")";
        }
    }
}
