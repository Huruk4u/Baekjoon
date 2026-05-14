import java.util.*;
import java.io.*;


class Solution {
    
    private int INF = 987654321;
    
    public int solution(int N, int M, int[][] edge_list, int K, int[] gps_log) {
        // dp[t][i]: t시간에 i번 노드에 위치할 경우, 이동 가능 경로를 만들 수 있는 최소 오류 수정 횟수
        int[][] dp = new int[K][N+1];
        for (int i = 0; i < K; i++) Arrays.fill(dp[i], INF);
        
        boolean[][] edges = new boolean[N+1][N+1];
        for (int i = 0; i < M; i++) {
            int u = edge_list[i][0], v = edge_list[i][1];
            edges[u][v] = true;
            edges[v][u] = true;
        }
        
        dp[0][gps_log[0]] = 0;
        for (int t = 1; t < K; t++) { // 100
            for (int curr = 1; curr < N+1; curr++) { // 200
                for (int prev = 1; prev < N+1; prev++) { // 200
                    if (!edges[prev][curr]) continue; // prev - curr 간선이 없는 경우는 건너뛴다.
                    
                    if (gps_log[t] != curr) { // 현재 노드가 로그에 기록된 노드의 위치와 다를 경우
                        dp[t][curr] = Integer.min(dp[t][curr], dp[t-1][prev] + 1);
                    } else {
                        dp[t][curr] = Integer.min(dp[t][curr], dp[t-1][prev]);
                    }
                }
            }
        }
        
        int temp = dp[K-1][gps_log[K-1]];
        if (temp == INF) return -1;
        else return temp;
    }
}