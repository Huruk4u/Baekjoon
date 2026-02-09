import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static boolean[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new boolean[N+1][N+1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u][v] = true;
            graph[v][u] = true;
        }

        PriorityQueue<ThreeNodes> heap = new PriorityQueue<>();
        for (int a = 1; a < N+1; a++) {
            for (int b = a+1; b < N+1; b++) {
                for (int c = b+1; c < N+1; c++) {
                   int rtn = checkUnlink(a, b, c);
                   if (rtn == 2) heap.add(new ThreeNodes(1, a, b, c));
                   else if (rtn == 1) heap.add(new ThreeNodes(0, a, b, c));
                }
            }
        }

        int answer = 0;
        while (!heap.isEmpty()) {
            ThreeNodes curr = heap.remove();
            if (checkUnlink(curr.a, curr.b, curr.c) == 0) continue;

            link(curr.a, curr.b, curr.c);
            answer += curr.weight;

            for (int x = 1; x < N+1; x++) {
                for (int y = x+1; y < N+1; y++) {
                    int rtn = checkUnlink(x, y, curr.a);
                    if (rtn == 2) heap.add(new ThreeNodes(1, x, y, curr.a));
                    else if (rtn == 1) heap.add(new ThreeNodes(0, x, y, curr.a));
                }
            }
            for (int x = 1; x < N+1; x++) {
                for (int y = x+1; y < N+1; y++) {
                    int rtn = checkUnlink(x, y, curr.b);
                    if (rtn == 2) heap.add(new ThreeNodes(1, x, y, curr.b));
                    else if (rtn == 1) heap.add(new ThreeNodes(0, x, y, curr.b));
                }
            }
            for (int x = 1; x < N+1; x++) {
                for (int y = x+1; y < N+1; y++) {
                    int rtn = checkUnlink(x, y, curr.c);
                    if (rtn == 2) heap.add(new ThreeNodes(1, x, y, curr.c));
                    else if (rtn == 1) heap.add(new ThreeNodes(0, x, y, curr.c));
                }
            }
        }
        System.out.println(answer);

        br.close();
    }

    private static void link(int a, int b, int c) {
        graph[a][b] = graph[b][a] = true;
        graph[b][c] = graph[c][b] = true;
        graph[a][c] = graph[c][a] = true;
    }

    private static int checkUnlink(int a, int b, int c) {
        if (a == b || b == c || a == c) return 0;
        int rtn = 0;
        if (!graph[a][b] || !graph[b][a]) rtn++;
        if (!graph[b][c] || !graph[c][b]) rtn++;
        if (!graph[c][a] || !graph[a][c]) rtn++;
        return rtn;
    }

    private static class ThreeNodes implements Comparable<ThreeNodes> {
        int weight, a, b, c;

        ThreeNodes(int weight, int a, int b, int c) {
            this.weight = weight;
            this.a = a;
            this.b = b;
            this.c = c;
        }
        @Override
        public int compareTo(ThreeNodes other) {
            return Integer.compare(this.weight, other.weight);
        }
        @Override
        public String toString() {
            return String.format("(%d, %d, %d, %d)", weight, a, b, c);
        }
    }
}
