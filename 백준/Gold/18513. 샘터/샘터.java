import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, K;

    private static HashMap<Long, Boolean> visited;

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
            long position = Long.parseLong(st.nextToken());
            queue.add(new Node(position, 0));
            visited.put(position, true);
        }
        System.out.println(bfs(queue));

        br.close();
    }

    private static long bfs(Queue<Node> queue) {
        int cnt = 0;
        long rtn = 0;
        long np;
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            if (curr.dist != 0) cnt++; // 현재 위치가 샘이 아니면 cnt를 한다.

            rtn += curr.dist;
            if (cnt == K) return rtn; // 모든 집을 찾았으면, 더이상 search를 하지 않는다.

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
        long position, dist;

        Node (long position, long dist) {
            this.position = position;
            this.dist = dist;
        }
    }
}
