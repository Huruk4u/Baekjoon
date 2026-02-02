import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, MAX_VELOCITY;

    private static boolean[] notNode;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        MAX_VELOCITY = N / 2;

        int[][] visited = new int[N+1][MAX_VELOCITY + 1];
        notNode = new boolean[N+1];
        for (int i = 0; i < M; i++) {
            int a = Integer.parseInt(br.readLine().trim());
            notNode[a] = true;
        }
        Queue<State> queue = new ArrayDeque();
        queue.add(new State(1, 0));
        System.out.println(bfs(queue, visited));

        br.close();
    }

    private static int bfs(Queue<State> queue, int[][] visited) {
        visited[queue.peek().number][queue.peek().velocity] = 1;
        while (!queue.isEmpty()) {
            State curr = queue.remove();
            if (curr.number == N) return visited[curr.number][curr.velocity] - 1;

            for (int i = -1; i <= 1; i++) {
                int nextVelocity = curr.velocity + i;
                int nextNumber = curr.number + nextVelocity;
                if (!inRange(nextNumber) || !inVelocityRange(nextVelocity) || visited[nextNumber][nextVelocity] != 0 || notNode[nextNumber]) continue;
                queue.add(new State(nextNumber, nextVelocity));
                visited[nextNumber][nextVelocity] = visited[curr.number][curr.velocity] + 1;
            }
        }
        return -1;
    }

    private static boolean inVelocityRange(int x) {
        return (0 < x && x <= MAX_VELOCITY);
    }

    private static boolean inRange(int x) {
        return (0 <= x && x < N+1);
    }

    private static class State {
        int number, velocity;

        State(int number, int velocity) {
            this.number = number;
            this.velocity = velocity;
        }
    }
}
