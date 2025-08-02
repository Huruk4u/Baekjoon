import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int answer;

    private static List<String> words;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        words = new ArrayList();

        for (int i = 0; i < N; i++) {
            String ipt = br.readLine().trim();
            words.add(ipt.substring(4, ipt.length() - 4));
        }

        answer = 0;
        if (K >= 5) {
            int temp = 532741;
            combination(0, 5, temp, K);
        }
        System.out.println(answer);
        br.close();
    }

    private static void combination(int idx, int depth, int temp, int K) {
        if (depth == K) {
            answer = Integer.max(answer, read(temp));
            return;
        }
        
        for (int i = idx; i < 26; i++) {
            if ((temp & (1 << i)) != 0) continue;
            combination(i + 1, depth + 1, temp ^ (1 << i), K);
        }
    }

    private static int read(int temp) {
        int rtn = 0;
        for (String word : words) {
            boolean flag = false;
            for (int i = 0; i < word.length(); i++) {
                if ((temp & 1 << (word.charAt(i) - 'a')) == 0) {
                    flag = true;
                    break;
                }
            }
            if (!flag) rtn++;
        }
        return rtn;
    }
}
