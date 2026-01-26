import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) Arrays.fill(dist[i], 987654321);
        for (int i = 0; i < N; i++) dist[i][i] = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < N; j++) dist[i][j] = Integer.parseInt(st.nextToken());
        }

        for (int k = 0; k < N; k++) {
            for (int u = 0; u < N; u++) {
                for (int v = 0; v < N; v++) {
                    dist[u][v] = Integer.min(dist[u][v], dist[u][k] + dist[k][v]);
                }
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            if (dist[A-1][B-1] <= C) System.out.println("Enjoy other party");
            else System.out.println("Stay here");
        }

        br.close();
    }
}
