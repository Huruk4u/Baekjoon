import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List<Integer>[] graph;

    private static int[] visited, listening, neighbors;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim());

        neighbors = new int[N+1];
        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int cnt = 0;
            while (true) {
                int j = Integer.parseInt(st.nextToken());
                if (j == 0) break;
                graph[i].add(j);
                cnt++;
            }
            neighbors[i] = cnt;
        }

        int M = Integer.parseInt(br.readLine().trim());
        Queue<Integer> queue = new ArrayDeque();

        visited = new int[N+1];
        listening = new int[N+1];
        Arrays.fill(visited, -1);

        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < M; i++) {
            int number = Integer.parseInt(st.nextToken());
            queue.add(number);
            visited[number] = 0;
        }

        bfs(queue);

        // output
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N+1; i++) {
            sb.append(visited[i] + " ");
        }
        System.out.println(sb.toString().trim());

        br.close();
    }

    private static void bfs(Queue<Integer> queue) {
        while (!queue.isEmpty()) {
            int curr = queue.remove();

            for (int next : graph[curr]) {
                if (visited[next] != -1) continue;
                listening[next]++;

                if (neighbors[next] % 2 == 0) {
                    if (listening[next] >= neighbors[next] / 2) {
                        visited[next] = visited[curr] + 1;
                        queue.add(next);
                    }
                } else {
                    if (listening[next] >= neighbors[next] / 2 + 1) {
                        visited[next] = visited[curr] + 1;
                        queue.add(next);
                    }
                }
            }
        }
        return;
    }
}
