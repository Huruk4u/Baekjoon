import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int[][] attacks = {
            {9, 3, 1}, {9, 1, 3}, {3, 9, 1}, {3, 1, 9}, {1, 9, 3}, {1, 3, 9}
    };

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        /////////////////////////// input
        int[] scv = new int[3];
        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) scv[i] = Integer.parseInt(st.nextToken());
        /////////////////////////// input

        int[][][] visited = new int[scv[0] + 1][scv[1] + 1][scv[2] + 1];
        Queue<Node> queue = new ArrayDeque<>();
        queue.add(new Node(scv[0], scv[1], scv[2]));

        System.out.println(bfs(queue, visited));

        br.close();
    }

    private static int bfs(Queue<Node> queue, int[][][] visited) {
        visited[queue.peek().scv1][queue.peek().scv2][queue.peek().scv3] = 1;
        while(!queue.isEmpty()) {
            Node curr = queue.remove();
            if (curr.scv1 == 0 && curr.scv2 == 0 && curr.scv3 == 0) return visited[0][0][0] - 1;

            for (int[] attack : attacks) {
                int nextScv1 = curr.scv1 - attack[0] >= 0? curr.scv1 - attack[0] : 0;
                int nextScv2 = curr.scv2 - attack[1] >= 0? curr.scv2 - attack[1] : 0;
                int nextScv3 = curr.scv3 - attack[2] >= 0? curr.scv3 - attack[2] : 0;

                if (visited[nextScv1][nextScv2][nextScv3] != 0) continue;

                visited[nextScv1][nextScv2][nextScv3] = visited[curr.scv1][curr.scv2][curr.scv3] + 1;
                queue.add(new Node(nextScv1, nextScv2, nextScv3));
            }
        }
        return -1;
    }

    private static class Node {
        int scv1, scv2, scv3;

        private Node(int scv1, int scv2, int scv3) {
            this.scv1 = scv1;
            this.scv2 = scv2;
            this.scv3 = scv3;
        }

        @Override
        public String toString() {
            return String.format("Node : %d %d %d", scv1, scv2, scv3);
        }
    }
}
