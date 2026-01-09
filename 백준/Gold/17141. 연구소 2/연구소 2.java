import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M;

    private static int[][] matrix;

    private static List<Point> startingPoints;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < N; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }

        startingPoints = new ArrayList();
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (matrix[y][x] == 2) startingPoints.add(new Point(y, x));
            }
        }
        boolean[] picked = new boolean[startingPoints.size()];
        int answer = backtracking(0, 0, picked);
        System.out.println(answer == INF? -1 : answer);

        br.close();
    }

    private static int bfs(Queue<Point> queue) {
        int[][] visited = new int[N][N];
        for (Point point : queue) visited[point.y][point.x] = 1;

        while (!queue.isEmpty()) {
            Point curr = queue.remove();

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx) || matrix[ny][nx] == 1 || visited[ny][nx] != 0) continue;
                visited[ny][nx] = visited[curr.y][curr.x] + 1;
                queue.add(new Point(ny, nx));
            }
        }

        int rtn = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (matrix[y][x] == 1) continue;
                if (visited[y][x] == 0) return -1;
                rtn = Integer.max(rtn, visited[y][x] - 1);
            }
        }
        return rtn;
    }

    private static int backtracking(int startingIdx, int depth, boolean[] picked) {
        if (depth == M) {
            Queue<Point> queue = new ArrayDeque();
            for (int i = 0; i < picked.length; i++) {
                if (picked[i]) queue.add(startingPoints.get(i));
            }
            int rtn = bfs(queue);
            return rtn == -1? INF : rtn;
        }

        int rtn = INF;
        for (int i = startingIdx; i < startingPoints.size(); i++) {
            picked[i] = true;
            rtn = Integer.min(rtn, backtracking(i+1, depth+1, picked));
            picked[i] = false;
        }

        return rtn;
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < N);
    }

    private static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public String toString() {
            return "(" + y + ", " + x + ")";
        }
    }
}
