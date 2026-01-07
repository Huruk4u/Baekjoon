import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static HashMap<String, List<String>> children;

    private static HashMap<String, Integer> inDeg;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String king = br.readLine().trim();

        HashMap<String, List<String>> children = new HashMap();
        HashMap<String, Double> blood = new HashMap();
        inDeg = new HashMap();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            String child = st.nextToken();
            String parent1 = st.nextToken();
            String parent2 = st.nextToken();

            if (!children.containsKey(parent1)) children.put(parent1, new ArrayList());
            if (!children.containsKey(parent2)) children.put(parent2, new ArrayList());

            children.get(parent1).add(child);
            children.get(parent2).add(child);

            if (!inDeg.containsKey(parent1)) inDeg.put(parent1, 0);
            if (!inDeg.containsKey(parent2)) inDeg.put(parent2, 0);

            if (!blood.containsKey(parent1)) blood.put(parent1, 0.0);
            if (!blood.containsKey(parent2)) blood.put(parent2, 0.0);

            inDeg.put(child, 2);
            blood.put(child, 0.0);
        }

        String[] nextKing = new String[M];
        for (int i = 0; i < M; i++) {
            nextKing[i] = br.readLine().trim();
        }

        PriorityQueue<Node> heap = new PriorityQueue();
        for (String parent : children.keySet()) {
            if (inDeg.get(parent) == 0) heap.add(new Node(parent));
        }

        blood.replace(king, 1.0);
        while (!heap.isEmpty()) {
            Node curr = heap.remove();
            if (!children.containsKey(curr.name)) continue;

            for (String child : children.get(curr.name)) {
                inDeg.replace(child, inDeg.get(child) - 1);
                blood.replace(child, blood.get(child) + blood.get(curr.name));
                if (inDeg.get(child) == 0) {
                    blood.replace(child, blood.get(child) / 2);
                    heap.add(new Node(child));
                }
            }
        }

        String answer = "";
        double temp = 0.0;
        for (String child : nextKing) {
            if (!blood.containsKey(child)) blood.put(child, 0.0);

            if (temp < blood.get(child)) {
                answer = child;
                temp = blood.get(child);
            }
        }
        System.out.println(answer);

        br.close();
    }

    private static class Node implements Comparable<Node> {
        String name;

        public Node(String name) {
            this.name = name;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(inDeg.get(this.name), inDeg.get(other.name));
        }

        @Override
        public String toString() {
            return name;
        }
    }
}
