import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, S;

    private static int[][] matrix;

    private static boolean[][] visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        /////////////////////////// input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < N; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine().trim());
        S = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        /////////////////////////// input

        Queue<Point> queue = new ArrayDeque();
        List<Point> virus = new ArrayList<>();
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) if (matrix[y][x] != 0) virus.add(new Point(y, x, matrix[y][x]));
        }

        Collections.sort(virus);
        visited = new boolean[N][N];

        for (Point point : virus) {
            visited[point.y][point.x] = true;
            queue.add(point);
        }
        bfs(queue);
        System.out.println(matrix[Y-1][X-1]);

        br.close();
    }

    private static void bfs(Queue<Point> queue) {
        for (int day = 0; day < S; day++) {

            int loop = queue.size();

            for (int dum = 0; dum < loop; dum++) {
                Point curr = queue.remove();

                for (int i = 0; i < 4; i++){
                    int ny = curr.y + dy[i];
                    int nx = curr.x + dx[i];
                    if (!inRange(ny, nx) || visited[ny][nx] || matrix[ny][nx] != 0) continue;

                    matrix[ny][nx] = curr.number;
                    visited[ny][nx] = true;
                    queue.add(new Point(ny, nx, curr.number));
                }
            }
        }
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < N);
    }

    private static class Point implements Comparable<Point> {
        int y, x, number;
        public Point(int y, int x, int number) {
            this.y = y;
            this.x = x;
            this.number = number;
        }

        @Override
        public int compareTo(Point other) {
            return Integer.compare(this.number, other.number);
        }
    }
}
