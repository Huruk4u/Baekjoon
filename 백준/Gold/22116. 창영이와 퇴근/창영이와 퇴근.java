import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    private static int[][] matrix, dist;

    private static int[] dy = {-1, 1, 0, 0}, dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        N = Integer.parseInt(br.readLine().trim());

        matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < N; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }

        // 최대 높이 차이의 절댓값이 최소인 경로
        dist = new int[N][N];
        for (int i = 0; i < N; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);

        PriorityQueue<Node> heap = new PriorityQueue<>();
        heap.add(new Node(0, 0, 0));

        System.out.println(dijkstra(heap));

        br.close();
    }

    private static int dijkstra(PriorityQueue<Node> heap) {
        dist[0][0] = 0;
        while (!heap.isEmpty()) {
            Node curr = heap.remove();
//            System.out.println(String.format("%d %d visited", curr.y, curr.x));
//            pprint(dist);

            if (curr.y == N-1 && curr.x == N-1) return curr.weight;

            if (dist[curr.y][curr.x] < curr.weight) continue;

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i], nx = curr.x + dx[i];
                if (!inRange(ny, nx)) continue;

                int nextDist = Math.max(dist[curr.y][curr.x], Math.abs(matrix[ny][nx] - matrix[curr.y][curr.x]));
                if (dist[ny][nx] <= nextDist) continue;
                dist[ny][nx] = nextDist;
                heap.add(new Node(ny, nx, dist[ny][nx]));
            }
        }
        return -1;
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < N);
    }

    private static class Node implements Comparable<Node> {
        int y, x, weight;
        Node (int y, int x, int weight) {
            this.y = y;
            this.x = x;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.weight, other.weight);
        }
    }

    private static void pprint(int[][] matrix) {
        for (int i = 0; i < N; i++) System.out.println(Arrays.toString(matrix[i]));
    }
}
