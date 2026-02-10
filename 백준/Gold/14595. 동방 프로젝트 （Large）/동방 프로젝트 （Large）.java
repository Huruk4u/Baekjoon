import java.io.*;
import java.util.*;

public class Main {

    private static int[] broken;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        broken = new int[N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            broken[u]++;
            broken[v]--;
        }

        for (int i = 1; i < N+1; i++) {
            broken[i] += broken[i-1];
        }

        int roomCnt = 0;
        for (int i = 1; i < N+1; i++) {
            if (broken[i] == 0) roomCnt++;
        }

        System.out.println(roomCnt);
    }
}
