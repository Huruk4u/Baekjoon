import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static char[][] matrix;

    private static int[] picked;

    private static int answer;

    private static int[] dy = {-1, 1, 0, 0};

    private static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        matrix = new char[5][5];
        for (int i = 0; i < 5; i++) matrix[i] = br.readLine().toCharArray();

        picked = new int[7];

        backtracking(0, 0, 0);
        System.out.println(answer);

        br.close();
    }

    private static void backtracking(int depth, int cntYeon, int start) {
        if (depth == 7) {
            if (bfs()) answer++;
            return;
        }

        for (int i = start; i < 25; i++) {
            if (matrix[i/5][i%5] == 'Y' && cntYeon + 1 == 4) {
                continue;
            }
            picked[depth] = i;
            if (matrix[i/5][i%5] == 'Y') {
                backtracking(depth+1, cntYeon+1, i+1);
            } else {
                backtracking(depth+1, cntYeon, i+1);
            }
        }
    }

    private static boolean bfs() {
        Queue<Node> queue = new ArrayDeque();
        queue.add(new Node(picked[0]/5, picked[0]%5));

        boolean[][] visited = new boolean[5][5];
        visited[queue.peek().y][queue.peek().x] = true;

        int cnt = 0;
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            cnt++;

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];

                for (int pick : picked) {
                    if (!inRange(ny, nx) || ny * 5 + nx != pick || visited[ny][nx]) continue;
                    visited[ny][nx] = true;
                    queue.add(new Node(ny, nx));
                }
            }
        }

        if (cnt == 7) return true;
        else return false;
    }

    private static class Node {
        int y, x;
        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < 5 && 0 <= x && x < 5);
    }
}
