import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine().trim());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine().trim());
            int N = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[][] dist = new int[N+1][N+1];
            for (int i = 0; i < N+1; i++) Arrays.fill(dist[i], INF);
            for (int i = 0; i < N+1; i++) dist[i][i] = 0;

            Friend[] friends = new Friend[P];
            for (int i = 0; i < P; i++) {
                st = new StringTokenizer(br.readLine().trim());
                friends[i] = new Friend(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }

            // graph define
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine().trim());
                int d = Integer.parseInt(st.nextToken());
                int l = Integer.parseInt(st.nextToken());
                int prev = Integer.parseInt(st.nextToken());
                for (int j = 0; j < l-1; j++) {
                    int curr = Integer.parseInt(st.nextToken());
                    dist[prev][curr] = d;
                    dist[curr][prev] = d;
                    prev = curr;
                }
            }

            // floyd-warshall
            for (int k = 1; k < N+1; k++) {
                for (int u = 1; u < N+1; u++) {
                    for (int v = 1; v < N+1; v++) {
                        dist[u][v] = Integer.min(dist[u][v], dist[u][k] + dist[k][v]);
                    }
                }
            }

            int answer = INF;
            for (int curr = 1; curr < N+1; curr++) {
                int temp = 0;
                for (Friend friend : friends) {
                    if (dist[curr][friend.cityNumber] == INF) {
                        temp = -1;
                        break;
                    }
                    temp = Integer.max(temp, dist[curr][friend.cityNumber] * friend.velocity);
                }

                if (temp == -1) continue;
                answer = Integer.min(answer, temp);
            }

            if (answer == INF) System.out.println(String.format("Case #%d: %d", t+1, -1));
            else System.out.println(String.format("Case #%d: %d", t+1, answer));
        }

        br.close();
    }

    private static class Friend {
        int cityNumber, velocity;
        Friend(int cityNumber, int velocity) {
            this.cityNumber = cityNumber;
            this.velocity = velocity;
        }
    }
}
