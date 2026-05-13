import java.util.*;
import java.io.*;


class Solution {

    private int N, M;
    
    int MOD = 20170805;
    
    private int[][] matrix;
    
    private int[][][] dp;
    
    private int[] dy = {1, 0}; // 하, 우
    
    private int[] dx = {0, 1};
    
    public int solution(int m, int n, int[][] cityMap) {
        N = cityMap.length;
        M = cityMap[0].length;
        matrix = cityMap;
        
        // dp[y][x][delta]: y, x 좌표에 delta 방향으로 접근했을 때 경로의 수;
        dp = new int[N][M][2];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }
        
        return backtracking(0, 0, 0);
    }
    
    private int backtracking(int cy, int cx, int prevDelta) {
        if (dp[cy][cx][prevDelta] != -1) return dp[cy][cx][prevDelta];
        if (cy == N-1 && cx == M-1) return 1;
        
        dp[cy][cx][prevDelta] = 0;
        
        if (matrix[cy][cx] == 2) {
            int ny = cy + dy[prevDelta];
            int nx = cx + dx[prevDelta];
            if (inRange(ny, nx) && matrix[ny][nx] != 1) {
                dp[cy][cx][prevDelta] = (dp[cy][cx][prevDelta] + backtracking(ny, nx, prevDelta)) % MOD;
            }
        } else {
            for (int currDelta = 0; currDelta < 2; currDelta++) {
                int ny = cy + dy[currDelta];
                int nx = cx + dx[currDelta];
                if (!inRange(ny, nx) || matrix[ny][nx] == 1) continue;
                dp[cy][cx][prevDelta] = (dp[cy][cx][prevDelta] + backtracking(ny, nx, currDelta)) % MOD;
            }
        }
        return dp[cy][cx][prevDelta];
    }
    
    private boolean inRange(int y, int x) {
        return (0 <= y && y < N) && (0 <= x && x < M);
    }
}