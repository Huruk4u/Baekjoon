import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int C, H;

    private static int[] parent;

    private static int[] power;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;

        power = new int[N+1];
        Arrays.fill(power, 1);

        List<int[]> ipts = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int[] ipt = new int[2];
            ipt[0] = Integer.parseInt(st.nextToken());
            ipt[1] = Integer.parseInt(st.nextToken());
            ipts.add(ipt);
        }

        st = new StringTokenizer(br.readLine().trim());
        C = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        for (int[] ipt : ipts) union(ipt[0], ipt[1]);

        boolean[] inHeap = new boolean[N+1];
        PriorityQueue<Node> heap = new PriorityQueue<>();
        for (int i = 1; i < N+1; i++) {
            if (find(i) == C || find(i) == H || inHeap[find(i)]) continue;
            int root = find(i);
            heap.add(new Node(root, power[root]));
            inHeap[root] = true;
        }

        int temp = 0;
        while (!heap.isEmpty() && temp < K) {
            temp++;
            Node curr = heap.remove();
            union(C, curr.number);
        }
        System.out.println(power[C]);

        br.close();
    }

    private static class Node implements Comparable<Node> {
        int number, power;

        public Node(int number, int power) {
            this.number = number;
            this.power = power;
        }

        @Override
        public int compareTo(Node other) {
            return -Integer.compare(power, other.power);
        }
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

        if (root_u == C || root_u == H) {
            parent[root_v] = root_u;
            power[root_u] += power[root_v];
            return;
        }
        if (root_v == C || root_v == H) {
            parent[root_u] = root_v;
            power[root_v] += power[root_u];
            return;
        }
        if (root_u < root_v) {
            parent[root_v] = root_u;
            power[root_u] += power[root_v];
        } else {
            parent[root_u] = root_v;
            power[root_v] += power[root_u];
        }
    }
}
