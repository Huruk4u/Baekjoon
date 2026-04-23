import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int N = schedules.length;
        
        int answer = 0;
        for (int i = 0; i < N; i++) {
            boolean flag = true;
            
            for (int j = 0; j < 7; j++) {
                flag &= getGift(schedules[i], timelogs[i][j], startday + j);
            }
            
            if (flag) answer++;
        }
        
        return answer;
    }
    
    private static boolean getGift(int target, int curr, int day) {
        if (day == 6 || day == 7 || day == 13) return true;
        
        int targetHour = target / 100;
        int targetMin = target % 100 + 10;
        if (targetMin >= 60) {
            targetHour++;
            targetMin %= 60;
        }
        int currHour = curr / 100;
        int currMin = curr % 100;
        
        if (targetHour > currHour) return true;
        if (targetHour == currHour) {
            if (targetMin >= currMin) return true;
        }
        return false;
    }
}