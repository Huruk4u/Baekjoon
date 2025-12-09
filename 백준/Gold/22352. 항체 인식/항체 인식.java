import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] before = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < M; j++) {
                before[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] after = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < M; j++) {
                after[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Outer: for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (before[y][x] == after[y][x]) continue;
                bfs(y, x, after[y][x], before);
                break Outer;
            }
        }

        boolean answer = true;
        Outer: for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (before[y][x] != after[y][x]) {
                    answer = false;
                    break Outer;
                }
            }
        }

        System.out.println(answer? "YES" : "NO");

        br.close();
    }

    private static void bfs(int y, int x, int data, int[][] matrix) {
        Queue<Point> queue = new ArrayDeque<>();
        queue.add(new Point(y, x));

        boolean[][] visited = new boolean[N][M];
        visited[y][x] = true;

        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                if (!inRange(ny, nx) || visited[ny][nx] || matrix[curr.y][curr.x] != matrix[ny][nx]) continue;

                queue.add(new Point(ny, nx));
                visited[ny][nx] = true;
            }
            matrix[curr.y][curr.x] = data;
        }
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < M);
    }
    private static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
