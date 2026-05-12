import java.io.*;
import java.util.*;


class Solution {
    
    private int N, M;
    
    private int[][] matrix;
    
    private int[] dy = {-1, 1, 0, 0};
    
    private int[] dx = {0, 0, -1, 1};
    
    public int solution(int[][] matrix) {
        N = matrix.length;
        M = matrix[0].length;
        
        this.matrix = matrix;
        
        Queue<Node> queue = new ArrayDeque();
        queue.add(new Node(0, 1, 0));

        return bfs(queue);
    }
    
    private int bfs(Queue<Node> queue) {
        int[][][] visited = new int[N][M][2];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Arrays.fill(visited[i][j], -1);
            }
        }
        visited[queue.peek().py][queue.peek().px][queue.peek().state] = 0;
        
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            if (curr.py == N-1 && curr.px == M-1) return visited[curr.py][curr.px][curr.state];
            
            // 헤드와 테일 부분 분리(편의용)
            int chy, chx, cty, ctx;
            if (curr.state == 0) { // 가로 상태
                chy = curr.py;
                chx = curr.px;
                cty = curr.py;
                ctx = curr.px - 1;
            } else { // 세로 상태
                chy = curr.py;
                chx = curr.px;
                cty = curr.py - 1;
                ctx = curr.px;
            }
            
            // 상하좌우 수평이동
            for (int i = 0; i < 4; i++) {
                int nhy = chy + dy[i];
                int nhx = chx + dx[i];
                int nty = cty + dy[i];
                int ntx = ctx + dx[i];
                
                if (!inRange(nhy, nhx) || !inRange(nty, ntx)) continue;
                if (visited[nhy][nhx][curr.state] != -1) continue;
                
                visited[nhy][nhx][curr.state] = visited[chy][chx][curr.state] + 1;
                queue.add(new Node(nhy, nhx, curr.state));
            }
            
            // 회전
            if (curr.state == 0) { // 가로 상태에 있는 경우
                // tail을 상회전시키기
                if (inRange(chy - 1, chx - 1) && inRange(chy - 1, chx)) {
                    int nhy = chy;
                    int nhx = chx;
                    if (visited[nhy][nhx][1] == -1) {
                        visited[nhy][nhx][1] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 1));
                    }
                }
                // tail을 하회전시키기
                if (inRange(chy + 1, chx - 1) && inRange(chy + 1, chx)) {
                    int nhy = chy + 1;
                    int nhx = chx;
                    if (visited[nhy][nhx][1] == -1) {
                        visited[nhy][nhx][1] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 1));
                    }
                }
                // head를 상회전시키기
                if (inRange(chy - 1, chx - 1) && inRange(chy - 1, chx)) {
                    int nhy = chy;
                    int nhx = chx - 1;
                    if (visited[nhy][nhx][1] == -1) {
                        visited[nhy][nhx][1] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 1));
                    }
                }
                // head를 하회전 시키기
                if (inRange(chy + 1, chx - 1) && inRange(chy + 1, chx)) {
                    int nhy = chy + 1;
                    int nhx = chx - 1;
                    if (visited[nhy][nhx][1] == -1) {
                        visited[nhy][nhx][1] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 1));
                    }
                }
            } else { // 세로 상태에 있는 경우
                // tail 좌회전 시키기
                if (inRange(chy - 1, chx - 1) && inRange(chy, chx - 1)) {
                    int nhy = chy;
                    int nhx = chx;
                    if (visited[nhy][nhx][0] == -1) {
                        visited[nhy][nhx][0] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 0));
                    }
                }
                // tail 우회전 시키기
                if (inRange(chy - 1, chx + 1) && inRange(chy, chx + 1)) {
                    int nhy = chy;
                    int nhx = chx + 1;
                    if (visited[nhy][nhx][0] == -1) {
                        visited[nhy][nhx][0] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 0));
                    }
                }
                // head 좌회전 시키기
                if (inRange(chy - 1, chx -1) && inRange(chy, chx - 1)) {
                    int nhy = cty;
                    int nhx = ctx;
                    if (visited[nhy][nhx][0] == -1) {
                        visited[nhy][nhx][0] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 0));
                    }
                }
                // head 우회전 시키기
                if (inRange(chy - 1, chx + 1) && inRange(chy, chx + 1)) {
                    int nhy = chy - 1;
                    int nhx = chx + 1;
                    if (visited[nhy][nhx][0] == -1) {
                        visited[nhy][nhx][0] = visited[chy][chx][curr.state] + 1;
                        queue.add(new Node(nhy, nhx, 0));
                    }
                }
            }
        }
        
        return -1;
    }
    
    private boolean inRange(int y, int x) {
        if (0 > y || y >= N || 0 > x || x >= M) return false;
        if (matrix[y][x] == 1) return false;
        return true;
    }
    
    private class Node {
        int py, px, state; // state 0: 가로 상태, state 1: 세로 상태
        
        private Node (int py, int px, int state) {
            this.py = py;
            this.px = px;
            this.state = state;
        }
        
        @Override
        public String toString() {
            return String.format("(%d, %d, %d)", py, px, state);
        }
    }
}