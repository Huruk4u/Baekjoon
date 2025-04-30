import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M, T;

    private static int[][] matrix;

    private static int[][][] visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        ///////////////////////////////// input
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }
        ///////////////////////////////// input

        visited = new int[N][M][2];
        Queue<Point> queue = new ArrayDeque<>(Arrays.asList(new Point(0, 0, 0)));

        int rtn = bfs(queue);

        if (rtn == -1) System.out.println("Fail");
        else System.out.println(rtn);

        br.close();
    }

    private static int bfs(Queue<Point> queue) {
        visited[queue.peek().y][queue.peek().x][0] = 1;
        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            if (visited[curr.y][curr.x][curr.state]-1 > T) continue;

            if (curr.y == N-1 && curr.x == M-1) return visited[curr.y][curr.x][curr.state] - 1;

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx)) continue;
                if (curr.state == 0 && matrix[ny][nx] == 1) continue;
                if (matrix[ny][nx] == 2) {
                    if (curr.state + 1 >= 2 || visited[ny][nx][curr.state + 1] != 0) continue;
                    visited[ny][nx][curr.state+1] = visited[curr.y][curr.x][curr.state] + 1;
                    queue.add(new Point(ny, nx, curr.state + 1));
                } else {
                    if (visited[ny][nx][curr.state] != 0) continue;
                    visited[ny][nx][curr.state] = visited[curr.y][curr.x][curr.state] + 1;
                    queue.add(new Point(ny, nx, curr.state));
                }

            }
        }
        return -1;
    }

    private static boolean inRange(int y, int x) {
        return 0 <= y && y < N && 0 <= x && x < M;
    }

    private static class Point {
        int y, x, state;
        public Point(int y, int x, int state) {
            this.y = y;
            this.x = x;
            this.state = state;
        }
    }
}
