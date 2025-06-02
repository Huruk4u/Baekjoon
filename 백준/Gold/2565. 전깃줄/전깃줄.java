import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        ///////////////////////////////////////// input
        int N = Integer.parseInt(br.readLine());

        List<Line> lines = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            lines.add(new Line(x, y));
        }
        ///////////////////////////////////////// input
        Collections.sort(lines);

        // dp 배열의 초기값을 1로 설정
        // dp[i] : i를 포함하는 최대 증가 부분수열
        int[] dp = new int[N];
        Arrays.fill(dp, 1);

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (lines.get(j).end <= lines.get(i).end) continue;
                dp[j] = Math.max(dp[j], dp[i] + 1);
            }
//            System.out.println(String.format("line %d번을 고려합니다.", i));
//            System.out.println(Arrays.toString(dp));
        }

//        System.out.println(Arrays.toString(dp));
        int max_line = Arrays.stream(dp).max().getAsInt();
        System.out.println(N - max_line);

        br.close();
    }

    private static class Line implements Comparable<Line> {
        int start, end;
        public Line(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Line other) {
            return Integer.compare(this.start, other.start);
        }

        @Override
        public String toString() {
            return String.format("%d %d", start, end);
        }
    }
}
