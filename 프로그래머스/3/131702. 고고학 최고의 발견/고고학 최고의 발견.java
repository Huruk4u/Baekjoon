import java.util.*;
import java.io.*;


class Solution {
    
    private int N, M;
    
    private int[] dy = {0, -1, 1, 0, 0};
    
    private int[] dx = {0, 0, 0, -1, 1};
    
    private int answer;
    
    public int solution(int[][] matrix) {
        N = matrix.length;
        M = matrix[0].length;
        answer = 987654321;
        
        // 1. 첫 줄 모든 경우의 수 구하기 4 ^ 8
        backtracking(0, matrix, new int[M]);
        
        return answer;
    }
    
    private int greedy(int turnCnt, int[][] matrix) {
        // 매트릭스 카피
        int[][] copyMatrix = new int[N][M];
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                copyMatrix[y][x] = matrix[y][x];
            }
        }
        
        for (int cy = 1; cy < N; cy++) {
            for (int cx = 0; cx < M; cx++) {
                for (int t = 0; t < 4; t++) {
                    if (copyMatrix[cy-1][cx] == 0) break;
                    
                    turnCnt++;
                    
                    for (int i = 0; i < 5; i++) {
                        int ny = cy + dy[i];
                        int nx = cx + dx[i];
                        if (!inRange(ny, nx)) continue;
                        copyMatrix[ny][nx] = (copyMatrix[ny][nx] + 1) % 4;
                    }
                }
            }
        }
        
        for (int x = 0; x < M; x++) {
            if (copyMatrix[N-1][x] != 0) return 987654321;
        }
        return turnCnt;
    }
    
    private void backtracking(int idx, int[][] matrix, int[] turnCnt) {
        if (idx == M) { // 여기서 그리디 코드 들어간다.
            int temp = 0;
            for (int i = 0; i < M; i++) temp += turnCnt[i];
            
            answer = Integer.min(answer, greedy(temp, matrix));
            return;
        }
        
        int cy = 0;
        int cx = idx;
        for (int t = 0; t < 4; t++) {
            for (int i = 0; i < 5; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                if (!inRange(ny, nx)) continue;
                matrix[ny][nx] = (matrix[ny][nx] + 1) % 4;
            }
            turnCnt[idx] = (t + 1) % 4;
            backtracking(idx + 1, matrix, turnCnt);
        }
    }
    
    private boolean inRange(int y, int x) {
        return (0 <= y && y < N) && (0 <= x && x < M);
    }
}