import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static String[][] matrix;

    private static boolean[][][] visited;

    private static int[] dy = {0, -1, 1, 0, 0, -1, -1, 1, 1};

    private static int[] dx = {0, 0, 0, -1, 1, -1, 1, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ipt;

        ///////////////////////////////////// input
        matrix = new String[8][8];
        for (int i = 0; i < 8; i++) {
            ipt = br.readLine().trim().split("");
            for (int j = 0; j < 8; j++) matrix[i][j] = ipt[j];
        }
        ///////////////////////////////////// input

        Queue<Point> runnerQueue = new ArrayDeque(Arrays.asList(new Point(7, 0, 0)));

        Queue<Point> wallQueue = new ArrayDeque();
        for (int y = 0; y < 8; y++) {
            for (int x = 0; x < 8; x++) if (matrix[y][x].equals("#")) wallQueue.add(new Point(y, x, 0));
        }

        visited = new boolean[8][8][9];
        visited[7][0][0] = true;

        int answer = bfs(runnerQueue, wallQueue);
        System.out.println(answer);

        br.close();
    }

    private static int bfs(Queue<Point> runnerQueue, Queue<Point> wallQueue) {
        while (true) {
//            System.out.println(String.format("---------------------- new day"));
//            pprint(matrix);
            //////////////////////////// 욱제 이동
            int runnerLoop = runnerQueue.size();
            for (int dum = 0; dum < runnerLoop; dum++) {
                Point curr = runnerQueue.remove();
//                System.out.println(String.format("%d %d visited", curr.y, curr.x));
                if (curr.y == 0 && curr.x == 7) return 1;

                for (int i = 0; i < 9; i++) {
                    int ny = curr.y + dy[i];
                    int nx = curr.x + dx[i];

                    if (!inRange(ny, nx) || matrix[ny][nx].equals("#")) continue;
                    runnerQueue.add(new Point(ny, nx, curr.day + 1));
                    visited[ny][nx][curr.day+1] = true;
                }
            }
//            System.out.println(runnerQueue);
            //////////////////////////// 욱제 이동

            //////////////////////////// 벽 이동
            boolean wallLive = false;
            String[][] newMatrix = new String[8][8];
            for (int i = 0; i < 8; i++) Arrays.fill(newMatrix[i], ".");
            for (int y = 0; y < 8; y++) {
                for (int x = 0; x < 8; x++) {
                    if (matrix[y][x].equals(".") || y+1 >= 8) continue;
                    newMatrix[y+1][x] = "#";
                    wallLive = true;
                }
            }
            if (!wallLive) return 1;

            matrix = newMatrix;
            //////////////////////////// 벽 이동
//            System.out.println(String.format("drop walls"));
//            pprint(matrix);
            /////////////////////////// 충돌 검사
            Queue<Point> nextRunnerQueue = new ArrayDeque();
            for (Point runner : runnerQueue) {
                if (matrix[runner.y][runner.x].equals("#")) continue;
                nextRunnerQueue.add(runner);
            }
            if (nextRunnerQueue.isEmpty()) return 0;
            runnerQueue = nextRunnerQueue;
            /////////////////////////// 충돌 검사
        }
    }

    private static void pprint(String[][] matrix) {
        for (int i = 0; i < matrix.length; i++) System.out.println(Arrays.toString(matrix[i]));
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < 8 && 0 <= x && x < 8);
    }

    private static class Point {
        int y, x, day;
        Point (int y, int x, int day) {
            this.y = y;
            this.x = x;
            this.day = day;
        }

        @Override
        public String toString() {
            return "Point [y=" + y + ", x=" + x + ", day=" + day + "]";
        }
    }
}
