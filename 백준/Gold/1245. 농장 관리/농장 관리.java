import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M;

    private static int[][] matrix;

    private static boolean[][] visited;

    private static int[] dy = {-1, 1, 0, 0, -1, -1, 1, 1};

    private static int[] dx = {0, 0, -1, 1, -1, 1, 1, -1};

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

        visited= new boolean[N][M];
        int answer = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (visited[y][x] || matrix[y][x] == 0) continue;
                Queue<Point> queue = new ArrayDeque(Arrays.asList(new Point(y, x)));
                boolean rtn = bfs(queue);
                if (rtn) {
                    answer++;
                }
            }
        }

        System.out.println(answer);

        br.close();
    }

    private static boolean bfs(Queue<Point> queue) {
        visited[queue.peek().y][queue.peek().x] = true;
        boolean isTop = true;
        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            for (int i = 0; i < 8; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx) || matrix[ny][nx] == 0) continue;
                if (matrix[ny][nx] != matrix[curr.y][curr.x]) {
                    if (matrix[ny][nx] > matrix[curr.y][curr.x]) {
                        isTop = false;
                        continue;
                    } else continue;
                }
                if (visited[ny][nx]) continue;

                visited[ny][nx] = true;
                queue.add(new Point(ny, nx));
            }
        }
        return isTop;
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

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < M);
    }
}
