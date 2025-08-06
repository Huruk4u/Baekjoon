import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int A, B, C;

    private static int[] MAX_CAP;

    private static boolean[][][] visited;

    private static Set<Integer> answerSet;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        MAX_CAP = new int[]{A, B, C};

        visited = new boolean[A+1][B+1][C+1];
        visited[0][0][C] = true;

        Queue<Node> queue = new ArrayDeque();
        queue.add(new Node(0, 0, C));

        answerSet = new TreeSet();
        bfs(queue);

        StringBuilder sb = new StringBuilder();
        for (int rtn : answerSet) sb.append(rtn + " ");
        System.out.println(sb.toString().trim());

        br.close();
    }

    private static void bfs(Queue<Node> queue) {
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            if (curr.a == 0) answerSet.add(curr.c);

//            System.out.println(queue);
//            System.out.println(String.format("%d %d %d visited", curr.a, curr.b, curr.c));

            int flood, nextA, nextB, nextC;

            // A -> B
            flood = Integer.min(B - curr.b, curr.a);
            nextA = curr.a - flood;
            nextB = curr.b + flood;
            if (!visited[nextA][nextB][curr.c]) {
                visited[nextA][nextB][curr.c] = true;
                queue.add(new Node(nextA, nextB, curr.c));
            }

            // A -> C
            flood = Integer.min(C - curr.c, curr.a);
            nextA = curr.a - flood;
            nextC = curr.c + flood;
            if (!visited[nextA][curr.b][nextC]) {
                visited[nextA][curr.b][nextC] = true;
                queue.add(new Node(nextA, curr.b, nextC));
            }

            // B -> A
            flood = Integer.min(A - curr.a, curr.b);
            nextB = curr.b - flood;
            nextA = curr.a + flood;
            if (!visited[nextA][nextB][curr.c]) {
                visited[nextA][nextB][curr.c] = true;
                queue.add(new Node(nextA, nextB, curr.c));
            }

            // B -> C
            flood = Integer.min(C - curr.c, curr.b);
            nextB = curr.b - flood;
            nextC = curr.c + flood;
            if (!visited[curr.a][nextB][nextC]) {
                visited[curr.a][nextB][nextC] = true;
                queue.add(new Node(curr.a, nextB, nextC));
            }

            // C -> A
            flood = Integer.min(A - curr.a, curr.c);
            nextC = curr.c - flood;
            nextA = curr.a + flood;
            if (!visited[nextA][curr.b][nextC]) {
                visited[nextA][curr.b][nextC] = true;
                queue.add(new Node(nextA, curr.b, nextC));
            }

            // C -> B
            flood = Integer.min(B - curr.b, curr.c);
            nextC = curr.c - flood;
            nextB = curr.b + flood;
            if (!visited[curr.a][nextB][nextC]) {
                visited[curr.a][nextB][nextC] = true;
                queue.add(new Node(curr.a, nextB, nextC));
            }
        }
    }


    private static class Node {
        int a, b, c;
        public Node(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public String toString() {
            return String.format("(%d %d %d)", a, b, c);
        }
    }
}
