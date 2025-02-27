import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		String[] ipt;
		for (int t = 0; t < T; t++) {
			ipt = br.readLine().split(" ");
			int N = Integer.parseInt(ipt[0]), M = Integer.parseInt(ipt[1]);

			List<Integer>[] graph = new ArrayList[N + 1];
			for (int i = 0; i < N + 1; i++) {
				graph[i] = new ArrayList<Integer>();
			}
			for (int i = 0; i < M; i++) {
				ipt = br.readLine().split(" ");
				int u = Integer.parseInt(ipt[0]), v = Integer.parseInt(ipt[1]);
				graph[u].add(v);
				graph[v].add(u);
			}

//			System.out.println(Arrays.toString(graph));
			boolean[] visited = new boolean[N + 1];

			String answer = "YES";
			boolean rtn = true;
			for (int i = 1; i < N + 1; i++) {
				if (visited[i]) continue;
				
				int[] union = new int[N + 1];
				union[i] = 1;
				
				Queue<Integer> queue = new LinkedList();
				queue.add(i);
				
				if (!isBinaryGraph(queue, graph, visited, union)) {
					answer = "NO";
					break;
				}
			}
			System.out.println(answer);
		}

		br.close();
	}

	public static boolean isBinaryGraph(Queue<Integer> queue, List<Integer>[] graph, boolean[] visited, int[] union) {
		visited[queue.peek()] = true;
		
		while (!queue.isEmpty()) {
			int curr = queue.remove();
			for (int next : graph[curr]) {
				if (union[curr] == union[next]) return false;
				if (union[curr] == 1) union[next] = 2;
				else union[next] = 1;
			}
			
			for (int next: graph[curr]) {
				if (visited[next]) continue;
				visited[next] = true;
				queue.add(next);
			}
		}
		return true;
	}
}