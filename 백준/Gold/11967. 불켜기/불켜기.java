import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static boolean[][] matrix, pathable;

    private static List<Point>[][] lightBtn;

    private static int N;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        lightBtn = new ArrayList[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) lightBtn[i][j] = new ArrayList();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;

            lightBtn[y][x].add(new Point(b, a));
        }

        matrix = new boolean[N][N];
        matrix[0][0] = true;

        pathable = new boolean[N][N];
        pathable[0][0] = true;

        Queue<Point> queue = new ArrayDeque();
        queue.add(new Point(0, 0));

        System.out.println(bfs(queue));

        br.close();
    }

    private static int bfs(Queue<Point> queue) {

        boolean[][] visited = new boolean[N][N];
        visited[0][0] = true;
        matrix[0][0] = true;

        int rtn = 1;
        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                if (!inRange(ny, nx)) continue;

                pathable[ny][nx] = true;
            }

            for (Point point : lightBtn[curr.y][curr.x]) {
                if (!matrix[point.y][point.x]) {
                    matrix[point.y][point.x] = true;
                    rtn++;
                }

                if (pathable[point.y][point.x] && !visited[point.y][point.x]) {
                    visited[point.y][point.x] = true;
                    queue.add(new Point(point.y, point.x));
                }
            }

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                if (!inRange(ny, nx) || visited[ny][nx] || !pathable[ny][nx] || !matrix[ny][nx]) continue;

                visited[ny][nx] = true;
                queue.add(new Point(ny, nx));
            }
        }
        return rtn;
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < N);
    }

    private static class Point {
        int y, x;
        private Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public String toString() {
            return "(" + x + "," + y + ")";
        }
    }
}
