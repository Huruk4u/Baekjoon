import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, M;

    private static int[][] matrix;

    private static int[][] visited;

    // 서, 북, 동, 남
    private static int[] dy = {0, -1, 0, 1};

    private static int[] dx = {-1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine().trim());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            for (int j = 0; j < M; j++) matrix[i][j] = Integer.parseInt(st.nextToken());
        }

        visited = new int[N][M];
        List<Integer> rooms = new ArrayList<>();
        int roomCnt = 0;
        int largestRoom = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (visited[y][x] != 0) continue;
                Queue<Point> queue = new ArrayDeque();
                queue.add(new Point(y, x));
                roomCnt++;
                rooms.add(bfs(queue, roomCnt));
                largestRoom = Integer.max(largestRoom, rooms.get(roomCnt - 1));
            }
        }

        int largestRoomCombine = 0;
        for (int cy = 0; cy < N; cy++) {
            for (int cx = 0; cx < M; cx++) {
                for (int i = 0; i < 4; i++) {
                    int ny = cy + dy[i];
                    int nx = cx + dx[i];
                    if (!inRange(ny, nx) || (matrix[cy][cx] & (1 << i)) == 0) continue;
                    if (visited[ny][nx] == visited[cy][cx]) continue;
                    largestRoomCombine = Integer.max(largestRoomCombine, rooms.get(visited[ny][nx] - 1) + rooms.get(visited[cy][cx] - 1));
                }
            }
        }

        System.out.println(roomCnt);
        System.out.println(largestRoom);
        System.out.println(largestRoomCombine);

        br.close();
    }

    // 가장 넓은 방의 크기
    private static int bfs(Queue<Point> queue, int roomNumber) {
        visited[queue.peek().y][queue.peek().x] = roomNumber;
        int rtn = 0;
        while (!queue.isEmpty()) {
            Point curr = queue.remove();
            rtn++;

            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                if (!inRange(ny, nx) || (matrix[curr.y][curr.x] & (1 << i)) != 0 || visited[ny][nx] != 0) continue;
                visited[ny][nx] = roomNumber;
                queue.add(new Point(ny, nx));
            }
        }
        return rtn;
    }

    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N && 0 <= x && x < M);
    }

    private static class Point {
        int y, x;
        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
