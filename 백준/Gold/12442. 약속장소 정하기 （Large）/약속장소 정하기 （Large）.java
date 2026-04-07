import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    private static int N;

    private static List<Edge>[] graph;

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine().trim());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine().trim());
            N = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            Friend[] friends = new Friend[P];
            for (int i = 0; i < P; i++) {
                st = new StringTokenizer(br.readLine().trim());
                friends[i] = new Friend(i, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }

            graph = new ArrayList[N+1];
            for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

            // graph define
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine().trim());
                int d = Integer.parseInt(st.nextToken());
                int l = Integer.parseInt(st.nextToken());
                int prev = Integer.parseInt(st.nextToken());
                for (int j = 0; j < l-1; j++) {
                    int curr = Integer.parseInt(st.nextToken());
                    graph[curr].add(new Edge(prev, d));
                    graph[prev].add(new Edge(curr, d));
                    prev = curr;
                }
            }

            int[][] distByFriends = new int[P][N+1];
            for (Friend friend : friends) {
                PriorityQueue<State> heap = new PriorityQueue();
                heap.add(new State(friend.cityNumber, 0));
                distByFriends[friend.number] = dijkstra(heap);
            }

            int answer = INF;
            for (int city = 1; city < N+1; city++) {
                int temp = 0;
                for (int i = 0; i < P; i++) {
                    if (distByFriends[i][city] == INF) {
                        temp = -1;
                        break;
                    }
                    temp = Integer.max(temp, distByFriends[i][city] * friends[i].velocity);
                }

                if (temp == -1) continue;
                answer = Integer.min(answer, temp);
            }

            if (answer == INF) System.out.println(String.format("Case #%d: %d", t+1, -1));
            else System.out.println(String.format("Case #%d: %d", t+1, answer));
        }

        br.close();
    }

    private static int[] dijkstra(PriorityQueue<State> heap) {
        int[] dist = new int[N+1];
        Arrays.fill(dist, INF);
        dist[heap.peek().number] = 0;

        while (!heap.isEmpty()) {
            State curr = heap.remove();

            if (dist[curr.number] < curr.cost) continue;

            for (Edge next: graph[curr.number]) {
                if (dist[next.number] <= curr.cost + next.weight) continue;

                dist[next.number] = curr.cost + next.weight;
                heap.add(new State(next.number, dist[next.number]));
            }
        }
        return dist;
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

    private static class Friend {
        int number, cityNumber, velocity;
        Friend(int number, int cityNumber, int velocity) {
            this.number = number;
            this.cityNumber = cityNumber;
            this.velocity = velocity;
        }
    }
}
