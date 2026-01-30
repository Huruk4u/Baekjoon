import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static boolean DONE = false;
    
    private static int[][] children;

    private static boolean[] visited;

    private static List<Integer> inOrderList, similarInOrderList;

    private static int N, INORDER_END, visitedCnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());

        children = new int[N+1][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int p = Integer.parseInt(st.nextToken());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            children[p][0] = left;
            children[p][1] = right;
        }

        inOrderList = new ArrayList();
        inOrder(1);
        INORDER_END = inOrderList.get(inOrderList.size()-1);

        visited = new boolean[N+1];
        similarInOrderList = new ArrayList();
        visitedCnt = 0;
        similarInOrder(1);

        br.close();
    }

    private static void inOrder(int curr) {
        if (children[curr][0] != -1) inOrder(children[curr][0]);
        inOrderList.add(curr);
        if (children[curr][1] != -1) inOrder(children[curr][1]);
    }

    private static void similarInOrder(int curr) {
        similarInOrderList.add(curr);

        if (!visited[curr]) {
            visited[curr] = true;
            visitedCnt++;
        }

        if (children[curr][0] != -1) {
            similarInOrder(children[curr][0]);
            similarInOrderList.add(curr);
        }
        if (children[curr][1] != -1) {
            similarInOrder(children[curr][1]);
            similarInOrderList.add(curr);
        }

        if (visitedCnt == N && curr == INORDER_END && !DONE) {
            System.out.println(similarInOrderList.size() - 1);
            DONE = true;
        }
    }
}
