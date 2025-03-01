import java.io.*;
import java.util.*;


public class Main {
	
	public static int[] dy = {-2, -2, 0, 0, 2, 2};
	
	public static int[] dx = {-1, 1, -2, 2, -1, 1};

	public static int[][] matrix = new int[200][200];
	
	public static int[][] visited = new int[200][200];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] ipt;
		ipt = br.readLine().split(" ");
		int sy = Integer.parseInt(ipt[0]), sx = Integer.parseInt(ipt[1]);
		int ty = Integer.parseInt(ipt[2]), tx = Integer.parseInt(ipt[3]);
		
//		System.out.println(String.format("%d %d %d %d", sy, sx, ty, tx));
		Queue<int[]> queue = new LinkedList();
		queue.add(new int[] {sy, sx});
		visited[sy][sx] = 1;
		System.out.println(bfs(queue, ty, tx));
		
		br.close();
	}
	
	public static int bfs(Queue<int[]> queue, int ty, int tx) {
		
		int [] curr;
		
		int cy, cx, ny, nx;
		
		while (!(queue.isEmpty())) {
			curr = queue.remove();
			cy = curr[0];
			cx = curr[1];
//			System.out.println(String.format("%d %d visited", cy, cx));
			if (cy == ty && cx == tx) return visited[cy][cx] - 1;
			
			for (int i = 0; i < 6; i++) {
				ny = cy + dy[i];
				nx = cx + dx[i];
				if (!inRange(ny, nx) || visited[ny][nx] != 0) continue;
				visited[ny][nx] = visited[cy][cx] + 1;
				queue.add(new int[] {ny, nx});
			}
		}
		return -1;
	}
	
	public static boolean inRange(int y, int x) {
		return (0 <= y && y < 200 && 0 <= x && x < 200);
	}
	
	public static void pprint() {
		for (int i = 0; i < 200; i++) {
			System.out.println(Arrays.toString(matrix[i]));
		}
	}
}
