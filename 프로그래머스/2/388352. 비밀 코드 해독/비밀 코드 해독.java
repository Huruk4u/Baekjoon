import java.util.*;
import java.io.*;


class Solution {
    
    private static int N;
    
    private static int[][] querys;
    
    private static int[] answers;
    
    public int solution(int n, int[][] query, int[] answer) {
        N = n;
        querys = query;
        answers = answer;
        
        return backtracking(1, 0, new int[5]);
    }
    
    private static int backtracking(int idx, int depth, int[] A) {
        if (depth == 5) {
            if (isPromising(A)) {
                return 1;
            } else {
                return 0;
            }
        }
        
        int rtn = 0;
        for (int i = idx; i <= N; i++) {
            A[depth] = i;
            rtn += backtracking(i + 1, depth + 1, A);
        }
        
        return rtn;
    }
    
    private static boolean isPromising(int[] A) {
        for (int i = 0; i < querys.length; i++) { // 10
            int[] query = querys[i];
            int temp = 0;
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) { // 25
                    if (A[j] == query[k]) temp++;
                }
            }
            
            if (temp != answers[i]) return false;
        }
        return true;
    }
}