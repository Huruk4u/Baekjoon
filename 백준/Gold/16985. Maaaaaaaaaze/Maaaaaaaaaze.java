import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<int[][]>[] matrixs;

    private static List<int[]> orders;

    private static boolean[] used;

    private static int answer;

    private static int[] dy = {-1, 1, 0, 0, 0, 0};
    private static int[] dx = {0, 0, -1, 1, 0, 0};
    private static int[] dz = {0, 0, 0, 0, -1, 1};

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        matrixs = new ArrayList[5];
        for (int i = 0; i < 5; i++) matrixs[i] = new ArrayList();

        for (int i = 0; i < 5; i++) {
            int[][] matrix = new int[5][5];
            for (int y = 0; y < 5; y++) {
                st = new StringTokenizer(br.readLine().trim());
                for (int x = 0; x < 5; x++) matrix[y][x] = Integer.parseInt(st.nextToken());
            }
            matrixs[i].add(matrix);
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 3; j++) {
                matrixs[i].add(rotate(matrixs[i].get(j)));
            }
        }

        orders = new ArrayList();
        used = new boolean[5];
        permutation(new int[5], 0);

        answer = INF;
        for (int[] order : orders) {
            combinationCube(order, 0, new int[5][5][5]);
        }

        System.out.println(answer == INF? -1 : answer);

        br.close();
    }

    private static int bfs(Queue<Point> queue, int[][][] cube) {
        int[][][] visited = new int[5][5][5];
        visited[0][0][0] = 1;
        while (!queue.isEmpty()) {
            Point curr = queue.remove();
            if (curr.y == 4 && curr.x == 4 && curr.z == 4) return visited[curr.z][curr.y][curr.x] - 1;

            for (int i = 0; i < 6; i++) {
                int nz = curr.z + dz[i];
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                if (!inRange(nz, ny, nx) || cube[nz][ny][nx] == 0 || visited[nz][ny][nx] != 0) continue;
                visited[nz][ny][nx] = visited[curr.z][curr.y][curr.x] + 1;
                queue.add(new Point(nz, ny, nx));
            }
        }
        return -1;
    }

    private static void combinationCube(int[] order, int depth, int[][][] cube) {
        if (depth == 5) {
            if (cube[0][0][0] == 0) return;
            Queue<Point> queue = new ArrayDeque();
            queue.add(new Point(0, 0, 0));

            int rtn = bfs(queue, cube);
            if (rtn == -1) return;
            answer = Integer.min(answer, rtn);
            return;
        }

        for (int i = 0; i < 4; i++) {
            cube[depth] = matrixs[order[depth]].get(i);
            combinationCube(order, depth+1, cube);
        }
    }

    private static void permutation(int[] order, int depth) {
        if (depth == 5) {
            int[] iptOrder = new int[5];
            for (int i = 0; i < 5; i++) iptOrder[i] = order[i];
            orders.add(iptOrder);
            return;
        }

        for (int i = 0; i < 5; i++) {
            if (used[i]) continue;
            used[i] = true;
            order[depth] = i;
            permutation(order, depth+1);
            used[i] = false;
        }
    }

    private static int[][] rotate(int[][] matrix) {
        int[][] rtn = new int[5][5];
        for (int y = 0; y < 5; y++) {
            for (int x = 0; x < 5; x++) {
                rtn[y][x] = matrix[4-x][y];
            }
        }
        return rtn;
    }

    private static boolean inRange(int z, int y, int x) {
        return (0 <= z && z < 5 && 0 <= y && y < 5 && 0 <= x && x < 5);
    }

    private static class Point {
        int z, y, x;
        public Point(int z, int y, int x) {
            this.z = z;
            this.y = y;
            this.x = x;
        }
    }
}
