import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static boolean[] isPrime;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // isPrime def
        isPrime = new boolean[300001];
        Arrays.fill(isPrime, true);

        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i < Math.sqrt(300001); i++) {
            for (int j = i * i; j < 300001; j += i) {
                isPrime[j] = false;
            }
        }

        int T = Integer.parseInt(br.readLine().trim());
        for (int t = 0; t < T; t++) {
            // input
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int N = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            Queue<Integer> queue= new ArrayDeque<>();
            queue.add(N);

            // answer
            System.out.println(bfs(queue, A, B, N));
        }
        br.close();
    }

    private static int bfs(Queue<Integer> queue, int low, int high, int N) {
        int[] visited = new int[1000001];
        Arrays.fill(visited, -1);
        visited[N] = 0;

        while (!queue.isEmpty()) {
            int curr = queue.remove();

            if (low <= curr && curr <= high && isPrime[curr]) return visited[curr];

            int next;
            next = curr / 2;
            if (inRange(next) && visited[next] == -1) {
                visited[next] = visited[curr] + 1;
                queue.add(next);
            }

            next = curr / 3;
            if (inRange(next) && visited[next] == -1) {
                visited[next] = visited[curr] + 1;
                queue.add(next);
            }

            next = curr + 1;
            if (inRange(next) && visited[next] == -1) {
                visited[next] = visited[curr] + 1;
                queue.add(next);
            }

            next = curr - 1;
            if (inRange(next) && visited[next] == -1) {
                visited[next] = visited[curr] + 1;
                queue.add(next);
            }
        }
        return -1;
    }

    private static boolean inRange(int x) {
        return 0 <= x && x < 1000001;
    }
}
