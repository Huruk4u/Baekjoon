import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, K, T;

    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken()); // 최대 거리 차이
        T = Integer.parseInt(st.nextToken()); // 최대 버전 차이

        List<Node> nodes = new ArrayList<>();
        st = new StringTokenizer(br.readLine().trim());
        int tx = Integer.parseInt(st.nextToken());
        int ty = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken()); // 버전 번호
        nodes.add(new Node(0, ty, tx, V));

        List<Node> startNodes = new ArrayList();
        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            nodes.add(new Node(i, y, x, v));
            if (p == 1) startNodes.add(nodes.get(i));
        }
        ////////////////////////// input

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;

        for (int u = 0; u < N+1; u++) {
            for (int v = u+1; v < N+1; v++) {
                if (u == v) continue;
                Node uNode = nodes.get(u);
                Node vNode = nodes.get(v);
                double dist = getDistance(uNode.y, uNode.x, vNode.y, vNode.x);
                if (dist <= (K * K) && Math.abs(uNode.version - vNode.version) <= T) {
                    union(uNode.number, vNode.number);
                }
            }
        } // 여기서 이을 수 있는 모든 간선이 이어진다.

        List<Integer> answer = new ArrayList();
        for (Node node : startNodes) {
            if (find(node.number) == 0) answer.add(node.number);
        }

        if (answer.isEmpty()){
            System.out.println(0);
        } else {
            StringBuilder sb = new StringBuilder();
            for (int number : answer) sb.append(number).append(" ");
            System.out.println(sb.toString().trim());
        }

        br.close();
    }

    private static int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private static void union(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);

        if (root_u == root_v) return;

        if (root_u == 0) {
            parent[root_v] = root_u;
            return;
        }
        if (root_v == 0) {
            parent[root_u] = root_v;
            return;
        }
        if (root_u < root_v) {
            parent[root_v] = root_u;
            return;
        } else {
            parent[root_u] = root_v;
            return;
        }
    }

    private static double getDistance(int y1, int x1, int y2, int x2) {
        return Math.pow(y1 - y2, 2) + Math.pow(x1 - x2, 2);
    }

    private static class Node {
        int number, y, x, version;

        Node(int number, int y, int x, int version) {
            this.number = number;
            this.y = y;
            this.x = x;
            this.version = version;
        }
    }
}
