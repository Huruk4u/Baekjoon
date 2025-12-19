import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M;

    private static List<Integer>[] graph;

    private static int[] team;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        team = new int[N+1];
        boolean answer = true;
        for (int i = 1; i < N+1; i++) {
            if (team[i] == 0) answer &= bfs(i);
        }
        System.out.println(answer? 1 : 0);

        br.close();
    }

    private static boolean bfs(int start) {
        Queue<Integer> queue = new ArrayDeque();
        queue.add(start);
        team[start] = 1;
        while (!queue.isEmpty()) {
            int curr = queue.remove();

            for (int next: graph[curr]) {
                if (team[next] == 0) {
                    if (team[curr] == 1) team[next] = 2;
                    else team[next] = 1;
                    queue.add(next);
                } else {
                    if (team[curr] == team[next]) return false;
                    else continue;
                }
            }
        }
        return true;
    }
}
