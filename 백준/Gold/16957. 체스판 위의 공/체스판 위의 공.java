import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int R, C;

    private static int[][] matrix, answer;

    private static Node[][] parent;

    private static int[] dy = {-1, 1, 0, 0, -1, -1, 1, 1};
    private static int[] dx = {0, 0, -1, 1, -1, 1, -1, 1};

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        matrix = new int[R][C];
        parent = new Node[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < C; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                parent[i][j] = new Node(i, j);
            }
        }

        answer = new int[R][C];
        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                solve(y, x);
            }
        }

        for (int y = 0; y < R; y++) {
            StringBuilder sb = new StringBuilder();
            for (int x = 0; x < C; x++) sb.append(answer[y][x]).append(" ");
            System.out.println(sb.toString().trim());
        }

        br.close();
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < R && 0 <= x && x < C);
    }

    private static void solve(int cy, int cx) {
        int temp = INF;
        Node next = new Node(-1, -1);
        for (int i = 0; i < 8; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];
            if (!inRange(ny, nx)) continue;
            if (matrix[ny][nx] < temp) {
                temp = matrix[ny][nx];
                next.y = ny;
                next.x = nx;
            }
        }

        if (temp >= matrix[cy][cx]) {
            answer[cy][cx] += 1;
        } else {
            next = union(new Node(cy, cx), new Node(next.y, next.x));
            solve(next.y, next.x);
        }
    }

    private static Node union(Node curr, Node next) {
        Node root_curr = find(curr);
        Node root_next = find(next);

        parent[root_curr.y][root_curr.x] = root_next;
        return root_next;
    }

    private static Node find(Node curr) {
        if (parent[curr.y][curr.x].y == curr.y && parent[curr.y][curr.x].x == curr.x) return curr;
        parent[curr.y][curr.x] = find(parent[curr.y][curr.x]);
        return parent[curr.y][curr.x];
    }

    private static class Node {
        int y, x;
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
        @Override
        public String toString() {
            return String.format("(%d, %d)", y, x);
        }
    }
}
