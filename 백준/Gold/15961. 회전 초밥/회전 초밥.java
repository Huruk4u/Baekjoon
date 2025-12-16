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
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] queue = new int[N * 2];
        for (int i = 0; i < N; i++) queue[i] = Integer.parseInt(br.readLine().trim());
        for (int i = N; i < N * 2; i++) queue[i] = queue[i - N];

        int[] dishes = new int[d+1];
        int answer = 0;
        for (int i = 0; i < k; i++) {
            if (dishes[queue[i]] == 0) answer++;
            dishes[queue[i]]++;
        }

        int left = 0, right = k-1;
        int temp = answer;
        while (left < N) {
            // left 전진
            if (dishes[queue[left]] - 1 == 0) temp--;
            dishes[queue[left]]--;
            left++;

            // right 전진
            if (dishes[queue[right + 1]] == 0) temp++;
            right++;
            dishes[queue[right]]++;

            if (dishes[c] == 0) answer = Integer.max(answer, temp+1);
            else answer = Integer.max(answer, temp);
        }
        System.out.println(answer);

        br.close();
    }
}
