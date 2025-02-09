import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		int[] count = new int[10001];
		
		for (int i = 0; i < N; i++) {
			count[Integer.parseInt(br.readLine())] ++;
		}
		
		for (int i = 0; i < 10001; i++) {
			while (count[i] != 0) {
				sb.append(i + "\n");
				count[i]--;
			}
		}
		
		bw.write(sb.toString());

		br.close();
		bw.flush();
	}
}
