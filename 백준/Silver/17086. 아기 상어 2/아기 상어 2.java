import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int[] dy = {1, -1, 0, 0, -1, 1, -1, 1};

    private static int[] dx = {0, 0, 1, -1, -1, -1, 1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        ////////////////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < M; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }
        ////////////////////////////////////// input

        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 1) continue;
                Queue<Node> queue = new ArrayDeque<>();
                queue.add(new Node(i, j));
                int temp = bfs(queue, matrix, N, M);
                answer = Integer.max(answer, temp);
            }
        }
        System.out.println(answer);

        br.close();
    }
    private static int bfs(Queue<Node> queue, int[][] matrix, int N, int M) {
        int[][] visited = new int[N][M];
        visited[queue.peek().y][queue.peek().x] = 1;
        while (!queue.isEmpty()) {
            Node curr = queue.remove();

            if (matrix[curr.y][curr.x] == 1) return visited[curr.y][curr.x] - 1;

            for (int i = 0; i < 8; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx, N, M) || visited[ny][nx] != 0) continue;
                visited[ny][nx] = visited[curr.y][curr.x] + 1;
                queue.add(new Node(ny, nx));
            }
        }
        return -1;
    }

    private static boolean inRange(int y, int x, int N, int M) {
        return (0 <= y && y < N && 0 <= x && x < M);
    }

    private static class Node {
        int y, x;
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
