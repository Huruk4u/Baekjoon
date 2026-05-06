import java.util.*;
import java.io.*;


class Solution {
    
    private int N;
    
    private int[][] dp;
    
    private int INF = 987654321;
    
    public int solution(int temp, int t1, int t2, int highCost, int lowCost, int[] onboard) {
        N = onboard.length;
        dp = new int[N][51]; // dp[시간][희망온도]
        
        temp += 10;
        t1 += 10;
        t2 += 10;
        
        for (int i = 0; i < N; i++) Arrays.fill(dp[i], INF);
        dp[0][temp] = 0;
        
        for (int i = 0; i < N-1; i++) {
            for (int t = 0; t < 51; t++) {
                if (onboard[i] == 1 && (t < t1 || t > t2)) continue;
                dp[i+1][t] = Integer.min(dp[i+1][t], dp[i][t] + lowCost);
                
                if (t - 1 >= 0) dp[i+1][t-1] = Integer.min(dp[i+1][t-1], dp[i][t] + highCost);
                if (t + 1 < 51) dp[i+1][t+1] = Integer.min(dp[i+1][t+1], dp[i][t] + highCost);
                
                if (temp == t) {
                    dp[i+1][t] = Integer.min(dp[i+1][t], dp[i][t]);
                } else if (temp > t) {
                    dp[i+1][t+1] = Integer.min(dp[i+1][t+1], dp[i][t]);
                } else {
                    dp[i+1][t-1] = Integer.min(dp[i+1][t-1], dp[i][t]);
                }
            }
        }
        
        int answer = INF;
        for (int i = 0; i < 51; i++) {
            if (onboard[N-1] == 1 && (i < t1 || i > t2)) continue;
            answer = Integer.min(answer, dp[N-1][i]);
        }
        
        
        return answer;
    }
}