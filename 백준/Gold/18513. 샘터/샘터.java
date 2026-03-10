import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, K;

    private static HashMap<Integer, Boolean> visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        Queue<Node> queue = new ArrayDeque<>();
        visited = new HashMap();
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) {
            int position = Integer.parseInt(st.nextToken());
            queue.add(new Node(position, 0));
            visited.put(position, true);
        }
        System.out.println(bfs(queue));

        br.close();
    }

    private static long bfs(Queue<Node> queue) {
        int cnt = 0;
        long rtn = 0;
        int np;
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            if (curr.dist != 0) cnt++;

            rtn += curr.dist;
            if (cnt == K) return rtn;

            np = curr.position - 1;
            if (!visited.containsKey(np)) {
                queue.add(new Node(np, curr.dist + 1));
                visited.put(np, true);
            }

            np = curr.position + 1;
            if (!visited.containsKey(np)) {
                queue.add(new Node(np, curr.dist + 1));
                visited.put(np, true);
            }
        }
        return -1;
    }

    private static class Node {
        int position, dist;

        Node (int position, int dist) {
            this.position = position;
            this.dist = dist;
        }
    }
}
