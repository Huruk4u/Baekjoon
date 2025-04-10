import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    private static int R, C;

    private static char[][] matrix;

    private static int[][] visited;

    private static int[] dy = {-1, 1, 0, 0}, dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ipt;

        ipt = br.readLine().trim().split(" ");
        R = Integer.parseInt(ipt[0]);
        C = Integer.parseInt(ipt[1]);

        matrix = new char[R][C];
        for (int i = 0; i < R; i++) {
            ipt = br.readLine().trim().split("");
            for (int j = 0; j < C; j++) matrix[i][j] = ipt[j].charAt(0);
        }

        visited = new int[R][C];

        Queue<Point> runnerQueue = new LinkedList();
        Queue<Point> fireQueue = new LinkedList();
        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                if (matrix[y][x] == 'J') runnerQueue.add(new Point(y, x));
                else if (matrix[y][x] == 'F') fireQueue.add(new Point(y, x));
            }
        }
        int answer = bfs(runnerQueue, fireQueue);

        if (answer == -1) System.out.println("IMPOSSIBLE");
        else System.out.println(answer);

        br.close();
    }

    private static int bfs(Queue<Point> runnerQueue, Queue<Point> fireQueue) {
        visited[runnerQueue.peek().y][runnerQueue.peek().x] = 1;
        while (!runnerQueue.isEmpty()) {

            int fireLoop = fireQueue.size();
            for (int dum = 0; dum < fireLoop; dum++) {
                Point curr = fireQueue.remove();
                for (int i = 0; i < 4; i++) {
                    int ny = curr.y + dy[i], nx = curr.x + dx[i];
                    if (inRange(ny, nx) && matrix[ny][nx] == '.') {
                        fireQueue.add(new Point(ny, nx));
                        matrix[ny][nx] = 'F';
                    }
                }
            }

//            System.out.println("------------------------------------");
//            pprintMatrix(matrix);

            int runnerLoop = runnerQueue.size();
            for (int dum = 0; dum < runnerLoop; dum++) {
                Point curr = runnerQueue.remove();

                for (int i = 0; i < 4; i++) {
                    int ny = curr.y + dy[i], nx = curr.x + dx[i];

                    if (!inRange(ny, nx)) return visited[curr.y][curr.x];

                    if (matrix[ny][nx] == '#' || matrix[ny][nx] == 'F' || visited[ny][nx] != 0) continue;
                    runnerQueue.add(new Point(ny, nx));
                    visited[ny][nx] = visited[curr.y][curr.x] + 1;
                }
            }

//            System.out.println();
//            pprintVisited(visited);
        }

        return -1;
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < R && 0 <= x && x < C);
    }

    private static class Point {
        int y, x;
        Point (int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public String toString() {
            return "Point{" +
                    "y=" + y +
                    ", x=" + x +
                    '}';
        }
    }

    private static void pprintMatrix(char[][] matrix) {
        for (int i = 0; i < R; i++) System.out.println(Arrays.toString(matrix[i]));
    }

    private static void pprintVisited(int[][] visited) {
        for (int i = 0; i < R; i++) System.out.println(Arrays.toString(visited[i]));
    }
}
