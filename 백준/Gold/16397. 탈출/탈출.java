import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());

        Queue<Integer> queue = new ArrayDeque();
        queue.add(N);
        int answer = bfs(queue, T, G);
        System.out.println(answer == -1? "ANG" : answer);

        br.close();
    }

    private static int bfs(Queue<Integer> queue, int T, int G) {
        int[] visited = new int[100000];
        visited[queue.peek()] = 1;
        while (!queue.isEmpty()) {
            int curr = queue.remove();
            if (visited[curr] - 1 > T) continue;
            if (curr == G) return visited[curr] - 1;

            // button A
            if (curr + 1 < 100000 && visited[curr + 1] == 0) {
                visited[curr + 1] = visited[curr] + 1;
                queue.add(curr + 1);
            }

            // button B
            int rtnB = buttonB(curr);
            if (rtnB < 100000 && visited[rtnB] == 0) {
                visited[rtnB] = visited[curr] + 1;
                queue.add(rtnB);
            }
        }
        return -1;
    }

    private static int buttonB(int n) {
        if (n * 2 >= 100000) return n * 2;

        char[] A = Integer.toString(n * 2).toCharArray();
        for (int i = 0; i < A.length; i++) {
            if (A[i] != '0') {
                A[i] = (char) (A[i] - 1);
                break;
            }
        }
        return Integer.parseInt(new String(A));
    }
}
