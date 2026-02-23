import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M, T;

    private static List<Edge>[] graph;

    private static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList<>();

        for (int i =0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));
        }

        PriorityQueue<State> heap = new PriorityQueue();
        heap.add(new State(1, 0));

        visited = new int[N+1];
        Arrays.fill(visited, -1);
        solve(heap);

        int answer = 0;
        for (int i = 1; i < N+1; i++) answer += visited[i];
        answer += T * (((N-1) * (N-2)) / 2);

        System.out.println(answer);

        br.close();
    }

    private static void solve(PriorityQueue<State> heap) {
        while (!heap.isEmpty()) {
            State curr = heap.remove();
            if (visited[curr.number] != -1) {
                continue;
            } else {
                visited[curr.number] = curr.cost;
            }

            for (Edge next : graph[curr.number]) {
                if (visited[next.number] != -1) continue;
                heap.add(new State(next.number, next.weight));
            }
        }
    }

    private static class State implements Comparable<State> {
        int number, cost;

        State(int number, int cost) {
            this.number = number;
            this.cost = cost;
        }

        @Override
        public int compareTo(State other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    private static class Edge {
        int number, weight;

        Edge(int number, int weight) {
            this.number = number;
            this.weight = weight;
        }
    }
}
