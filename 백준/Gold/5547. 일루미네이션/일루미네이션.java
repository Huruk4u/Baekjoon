import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int W, H;

    private static int[][] matrix;

    private static int[][] oddDelta = {{0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 0}};
    
    private static int[][] evenDelta = {{-1, -1}, {0, -1}, {1, 0}, {0, 1}, {-1, 1}, {-1, 0}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        matrix = new int[H+2][W+2];
        for (int y = 1; y < H+1; y++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int x = 1; x < W+1; x++) {
                matrix[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        Queue<Point> queue = new ArrayDeque<>();
        queue.add(new Point(0, 0));
        System.out.println(bfs(queue));
        br.close();
    }

    private static int bfs(Queue<Point> queue) {
        boolean[][] visited = new boolean[H+2][W+2];
        visited[0][0] = true;

        int rtn = 0;
        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            if (curr.y % 2 == 1) { // use odd
                for (int[] delta : oddDelta) {
                    int ny = curr.y + delta[1];
                    int nx = curr.x + delta[0];
                    if (!inRange(ny, nx) || visited[ny][nx]) continue;
                    if (matrix[ny][nx] == 1) {
                        rtn++;
                    } else {
                        visited[ny][nx] = true;
                        queue.add(new Point(ny, nx));
                    }
                }
            } else { // use even
                for (int[] delta : evenDelta) {
                    int ny = curr.y + delta[1];
                    int nx = curr.x + delta[0];
                    if (!inRange(ny, nx) || visited[ny][nx]) continue;
                    if (matrix[ny][nx] == 1) {
                        rtn++;
                    } else {
                        visited[ny][nx] = true;
                        queue.add(new Point(ny, nx));
                    }
                }
            }
        }
        return rtn;
    }

    private static class Point {
        int y, x;

        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < H+2) && (0 <= x && x < W+2);
    }
}
