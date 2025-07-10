import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static long[] A, tree, lazy;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        /////////////////////////////////// input
        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        A = new long[N];
        for (int i = 0; i < N; i++) A[i] = Long.parseLong(br.readLine().trim());
        /////////////////////////////////// input

        tree = new long[4 * N + 1];
        lazy = new long[4 * N + 1];

        define(1, 0, N-1);
        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int token = Integer.parseInt(st.nextToken());
            if (token == 1) {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                long value = Long.parseLong(st.nextToken());
                update(1, left-1, right-1, 0, N-1, value);
            } else {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                System.out.println(query(1, left-1, right-1, 0, N-1));
            }
        }

        br.close();
    }

    private static long define(int node, int left, int right) {
        if (left == right) {
            tree[node] = A[left];
            return tree[node];
        }
        int mid = (left + right) / 2;

        long leftVal = define(node * 2, left, mid);
        long rightVal = define(node * 2 + 1, mid + 1, right);

        tree[node] = leftVal + rightVal;
        return tree[node];
    }

    private static long query(int node, int queryLeft, int queryRight, int start, int end) {
        propagate(node, start, end);
        if (end < queryLeft || start > queryRight) return 0;
        if (queryLeft <= start && end <= queryRight) return tree[node];

        int mid = (start + end) / 2;
        long leftVal = query(node * 2, queryLeft, queryRight, start, mid);
        long rightVal = query(node * 2 + 1, queryLeft, queryRight, mid + 1, end);

        return leftVal + rightVal;
    }

    private static void update(int node, int updateLeft, int updateRight, int start, int end, long value) {
        propagate(node, start, end);
        // 범위 밖으로 완전히 벗어나는 경우, update할 범위가 아니므로 return
        if (end < updateLeft || start > updateRight) return;
        // 범위 안으로 완전히 들어온 경우, update할 범위에 완전히 들어온 것이므로 lazy배열을 갱신한다.
        if (updateLeft <= start && end <= updateRight) {
            lazy[node] += value;
            propagate(node, start, end);
            return;
        }
        int mid = (start + end) / 2;
        update(node * 2, updateLeft, updateRight, start, mid, value);
        update(node * 2 + 1, updateLeft, updateRight, mid + 1, end, value);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    private static void propagate(int node, int start, int end) {
        if (lazy[node] == 0) return;
        // 리프노드가 아니라면
        if (start != end) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        tree[node] += (end - start + 1) * lazy[node];
        lazy[node] = 0;
    }
}
