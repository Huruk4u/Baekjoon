import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int[] A, tree, lazy;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim());
        st = new StringTokenizer(br.readLine());
        A = new int[N];
        for (int i = 0; i < N; i++) A[i] = Integer.parseInt(st.nextToken());

        tree = new int[4 * N];
        lazy = new int[4 * N];

        define(1, 0, N-1);

        int M = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int token = Integer.parseInt(st.nextToken());
            if (token == 1) {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                int value = Integer.parseInt(st.nextToken());

                if (left > right) update(1, right, left, 0, N-1, value);
                else update(1, left, right, 0, N-1, value);

            } else {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                if (left > right) System.out.println(query(1, right, left, 0, N-1));
                else System.out.println(query(1, left, right, 0, N-1));
            }
        }

        br.close();
    }

    private static int define(int node, int left, int right) {
        if (left == right) {
            tree[node] = A[left];
            return tree[node];
        }

        int mid = (left + right) / 2;

        int leftVal = define(node * 2, left, mid);
        int rightVal = define(node * 2 + 1, mid + 1, right);

        tree[node] = leftVal ^ rightVal;
        return tree[node];
    }

    private static int query(int node, int queryLeft, int queryRight, int left, int right) {
        propagation(node, left, right);
        if (right < queryLeft || left > queryRight) return 0;
        if (queryLeft <= left && right <= queryRight) return tree[node];

        int mid = (left + right) / 2;

        int leftVal = query(node * 2, queryLeft, queryRight, left, mid);
        int rightVal = query(node * 2 + 1, queryLeft, queryRight, mid + 1, right);

        return leftVal ^ rightVal;
    }

    private static void update(int node, int updateLeft, int updateRight, int left, int right, int value) {
        propagation(node, left, right);
        if (right < updateLeft || left > updateRight) return;
        if (updateLeft <= left && right <= updateRight) {
            lazy[node] ^= value;
            propagation(node, left, right);
            return;
        }

        int mid = (left + right) / 2;
        update(node * 2, updateLeft, updateRight, left, mid, value);
        update(node * 2 + 1, updateLeft, updateRight, mid + 1, right, value);

        tree[node] = tree[node * 2] ^ tree[node * 2 + 1];
        return;
    }

    private static void propagation(int node, int left, int right) {
        if (lazy[node] == 0) return;
        if (left != right) {
            lazy[node * 2] ^= lazy[node];
            lazy[node * 2 + 1] ^= lazy[node];
        }
        if ((right - left + 1) % 2 == 1) tree[node] ^= lazy[node];
        lazy[node] = 0;
    }
}
