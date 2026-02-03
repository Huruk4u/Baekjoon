import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<Integer>[] graph;

    private static int[] fruits;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim());

        fruits = new int[N+1];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 1; i < N+1; i++) fruits[i] = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        int[] visited = new int[N+1];
        Arrays.fill(visited, -1);
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(1);
        bfs(queue, visited);

        int u = 0, temp = -1;
        for (int i = 1; i < N+1; i++) {
            if (temp < visited[i]) {
                temp = visited[i];
                u = i;
            }
        }

        visited = new int[N+1];
        Arrays.fill(visited, -1);
        queue = new ArrayDeque();
        queue.add(u);
        bfs(queue, visited);

        temp = -1;
        int v = 1;
        for (int i = 1; i < N+1; i++) {
            if (temp < visited[i]) {
                temp = visited[i];
                v = i;
            }
        }
        System.out.println(String.format("%d %d", temp, Integer.min(u, v)));

        br.close();
    }

    private static void bfs(Queue<Integer> queue, int[] visited) {
        visited[queue.peek()] = fruits[queue.peek()];
        while (!queue.isEmpty()) {
            int curr = queue.remove();
            for (int next : graph[curr]) {
                if (visited[next] != -1) continue;
                visited[next] = visited[curr] + fruits[next];
                queue.add(next);
            }
        }
        return;
    }
}
