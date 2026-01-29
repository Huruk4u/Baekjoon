import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;
    private static List<Integer>[] graph;
    private static Node[] nodes;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            N = Integer.parseInt(br.readLine().trim());
            if (N == 0) break;

            graph = new ArrayList[N+1];
            for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

            nodes = new Node[N+1];

            graph[0].add(1);
            for (int u = 1; u < N+1; u++) {
                st = new StringTokenizer(br.readLine().trim());
                char type = st.nextToken().charAt(0);
                int weight = Integer.parseInt(st.nextToken());
                while (true) {
                    int v = Integer.parseInt(st.nextToken());
                    if (v == 0) break;
                    graph[u].add(v);
                }
                nodes[u] = new Node(type, u, weight);
            }

            Queue<State> queue = new ArrayDeque();
            queue.add(new State(0, 0));

            if (bfs(queue)) System.out.println("Yes");
            else System.out.println("No");
        }

        br.close();
    }

    private static boolean bfs(Queue<State> queue) {
        boolean[][] visited = new boolean[N+1][501];
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            State curr = queue.remove();
            if (curr.nodeNumber == N) return true;

            for (Integer next : graph[curr.nodeNumber]) {
                Node nextNode = nodes[next];
                if (nextNode.type == 'T') { // 트롤 만났을 때
                    if (curr.coin < nextNode.weight) continue;
                    if (visited[next][curr.coin - nextNode.weight]) continue;
                    visited[next][curr.coin - nextNode.weight] = true;
                    queue.add(new State(next, curr.coin - nextNode.weight));
                } else if (nextNode.type == 'L') { // 레프리콘 만났을 때
                    int nextCoin = curr.coin;
                    if (curr.coin < nextNode.weight) nextCoin = nextNode.weight;
                    if (visited[next][nextCoin]) continue;
                    visited[next][nextCoin] = true;
                    queue.add(new State(next, nextCoin));
                } else { // 빈 방
                    if (visited[next][curr.coin]) continue;
                    visited[next][curr.coin] = true;
                    queue.add(new State(next, curr.coin));
                }
            }
        }
        return false;
    }

    private static class State {
        int nodeNumber, coin;
        State(int nodeNumber, int coin) {
            this.nodeNumber = nodeNumber;
            this.coin = coin;
        }

        @Override
        public String toString() {
            return "(" + nodeNumber + " " + coin + ")";
        }
    }

    private static class Node {
        char type;
        int number, weight;
        Node(char type, int number, int weight) {
            this.type = type;
            this.number = number;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return "(" + type + " " + number + " " + weight + ")";
        }
    }
}
