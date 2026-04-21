import java.util.*;
import java.io.*;


class Solution {
    public int solution(int[][] signals) {
        int N = 1;
        for (int i = 0; i < signals.length; i++) {
            N *= (signals[i][0] + signals[i][1] + signals[i][2]);
        }
        
        int[] A = new int[N+1];
        for (int i = 0; i < signals.length; i++) {
            int jump = signals[i][0] + signals[i][1] + signals[i][2];
            for (int j = 1; j < N+1; j += jump) {
                for (int duration = 0; duration < signals[i][1]; duration++) {
                    A[j+signals[i][0]+duration]++;
                }
            }
        }
        
        int answer = -1;
        for (int i = 1; i < N + 1; i++) {
            if (A[i] == signals.length) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}