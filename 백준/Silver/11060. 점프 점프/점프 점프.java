import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    private static int[] A;

    private static int[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        N = Integer.parseInt(br.readLine().trim());

        A = new int[N];

        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) A[i] = Integer.parseInt(st.nextToken());

        visited = new int[N];
        Queue<Integer> queue = new ArrayDeque<>(Arrays.asList(0));

        System.out.println(bfs(queue));

        br.close();
    }

    private static int bfs(Queue<Integer> queue) {
        visited[queue.peek()] = 1;
        while (!queue.isEmpty()) {
            int curr = queue.remove();
            if (curr == N-1) return visited[curr] - 1;

            for (int jump = 1; jump < A[curr] + 1; jump++) {
                if (!inRange(curr + jump) || visited[curr + jump] != 0) continue;
                queue.add(curr + jump);
                visited[curr + jump] = visited[curr] + 1;
            }
        }
        return -1;
    }


    private static boolean inRange(int x) {
        return (x < N);
    }
}
