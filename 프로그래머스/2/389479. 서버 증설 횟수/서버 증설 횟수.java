import java.util.*;
import java.io.*;


class Solution {
    public int solution(int[] players, int m, int k) {
        int[] servers = new int[24];
        
        int result = 0;
        for (int i = 0; i < 24; i++) {
            if (players[i] / m < servers[i] + 1) continue;
            
            int dummy = players[i] / m - servers[i]; // 증설해야 하는 서버 갯수
            
            for (int j = 0; j < k; j++) {
                if (i + j >= 24) break;
                servers[i + j] += dummy;
            }
            
            result += dummy;
        }
        
        return result;
    }
}