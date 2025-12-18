import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;

    private static List<Integer>[] graph;

    private static int[] team;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine().trim());

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) graph[i] = new ArrayList();
        for (int u = 0; u < N; u++) {
            st = new StringTokenizer(br.readLine().trim());
            int lenIpt = Integer.parseInt(st.nextToken());
            for (int j = 0; j < lenIpt; j++) {
                int v = Integer.parseInt(st.nextToken()) - 1;
                graph[u].add(v);
            }
        }

        team = new int[N];

        for (int i = 0; i < N; i++) {
            if (team[i] == 0) {
                bfs(i);
            }
        }

        StringBuilder team1 = new StringBuilder();
        StringBuilder team2 = new StringBuilder();
        int team1Cnt = 0, team2Cnt = 0;
        for (int i = 0; i < N; i++) {
            if (team[i] == 1) {
                team1.append(i+1 + " ");
                team1Cnt++;
            } else {
                team2.append(i+1 + " ");
                team2Cnt++;
            }
        }

        System.out.println(team1Cnt);
        System.out.println(team1.toString().trim());
        System.out.println(team2Cnt);
        System.out.println(team2.toString().trim());

        br.close();
    }

    private static boolean bfs(int start) {
        Queue<Integer> queue = new ArrayDeque();
        queue.add(start);
        team[start] = 1;
        while (!queue.isEmpty()) {
            int curr = queue.remove();

            for (int next : graph[curr]) {
                if (team[next] != 0) continue;

                if (team[curr] == 1) team[next] = 2;
                else team[next] = 1;

                queue.add(next);
            }
        }
        return true;
    }
}
