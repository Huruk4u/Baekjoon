import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int INF = 987654321;
    
    private static int[][] dist;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        int T = Integer.parseInt(br.readLine().trim());
        for (int t = 0; t < T; t++) {
            ///////////////////////////////////// input
            st = new StringTokenizer(br.readLine().trim());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            dist = new int[N + 1][N + 1];
            for (int i = 1; i < N + 1; i++) Arrays.fill(dist[i], INF);
            for (int i = 1; i < N + 1; i++) dist[i][i] = 0;

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine().trim());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());

                dist[u][v] = w;
                dist[v][u] = w;
            }

            int K = Integer.parseInt(br.readLine().trim());

            int[] friends = new int[K];
            st = new StringTokenizer(br.readLine().trim());
            for (int i = 0; i < K; i++) friends[i] = Integer.parseInt(st.nextToken());
            ///////////////////////////////////// input

            for (int k = 1; k < N+1; k++) {
                for (int u = 1; u < N+1; u++) {
                    for (int v = 1; v < N+1; v++) {
                        dist[u][v] = Math.min(dist[u][v], dist[u][k] + dist[k][v]);
                    }
                }
            }
            
            int answer = 0;
            int answer_weight = INF;
            for (int curr = 1; curr < N+1; curr++) {
                int temp = 0;
                for (int friend : friends) temp += dist[curr][friend];

                if (temp < answer_weight) {
                    answer = curr;
                    answer_weight = temp;
                }
            }

            System.out.println(answer);
        }

        br.close();
    }

    private static class Edge implements Comparable<Edge> {
        int number, weight;
        Edge(int number, int weight) {
            this.number = number;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.weight, other.weight);
        }
    }
}
