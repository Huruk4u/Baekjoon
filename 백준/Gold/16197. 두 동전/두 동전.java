import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;

    private static int[][] matrix;

    private static int[][][][] visited;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ///////////////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        char[][] ipt = new char[N][M];
        for (int i = 0; i < N; i++) ipt[i] = br.readLine().toCharArray();

        matrix = new int[N][M];
        int y1 = -1, x1 = -1, y2 = -1, x2 = -1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (ipt[i][j] == '#') matrix[i][j] = 1;
                else if (ipt[i][j] == 'o') {
                    if (y1 == -1 && x1 == -1){
                        y1 = i;
                        x1 = j;
                    } else {
                        y2 = i;
                        x2 = j;
                    }
                }
            }
        }

        Queue<Node> queue = new ArrayDeque();
        queue.add(new Node(y1, x1, y2, x2));

        visited = new int[20][20][20][20];
        visited[y1][x1][y2][x2] = 1;
        ///////////////////////////////////// input

        int answer = bfs(queue);
        System.out.println(answer);

        br.close();
    }

    private static int bfs(Queue<Node> queue) {
        while(!queue.isEmpty()) {
            Node curr = queue.remove();
            if (visited[curr.y1][curr.x1][curr.y2][curr.x2] == 11) continue;

            for (int i = 0; i < 4; i++) {
                int ny1 = curr.y1 + dy[i];
                int nx1 = curr.x1 + dx[i];
                int ny2 = curr.y2 + dy[i];
                int nx2 = curr.x2 + dx[i];
                if (!inRange(ny1, nx1) && !inRange(ny2, nx2)) continue;
                else {
                    if (!inRange(ny1, nx1) || !inRange(ny2, nx2)) return visited[curr.y1][curr.x1][curr.y2][curr.x2];
                    int rny1 = ny1, rnx1 = nx1, rny2 = ny2, rnx2 = nx2;
                    if (matrix[ny1][nx1] == 1) {
                        rny1 = curr.y1;
                        rnx1 = curr.x1;
                    }
                    if (matrix[ny2][nx2] == 1) {
                        rny2 = curr.y2;
                        rnx2 = curr.x2;
                    }
                    if (visited[rny1][rnx1][rny2][rnx2] != 0) continue;
                    visited[rny1][rnx1][rny2][rnx2] = visited[curr.y1][curr.x1][curr.y2][curr.x2] + 1;
                    queue.add(new Node(rny1, rnx1, rny2, rnx2));
                }
            }
        }
        return -1;
    }

    private static boolean inRange(int y, int x) {
        return 0 <= y && y < N && 0 <= x && x < M;
    }

    private static class Node {
        int y1, x1, y2, x2;
        public Node(int y1, int x1, int y2, int x2) {
            this.y1 = y1;
            this.x1 = x1;
            this.y2 = y2;
            this.x2 = x2;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)-(%d, %d)", y1, x1, y2, x2);
        }
    }
}
