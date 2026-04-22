import java.util.*;
import java.io.*;


class Solution {
    public int solution(int n, int w, int num) {
        int remainFloor = (n % w == 0)? n / w - 1 : n / w;
        int targetFloor = (num % w == 0)? num / w - 1 : num / w;
        
        System.out.println(String.format("remainFloor : %d, targetFloor : %d", remainFloor, targetFloor));
        int result = remainFloor - targetFloor; // 최소로 걷어내야 하는 상자의 수
        
        if (n % w == 0) return result + 1;
        
        if (isSameDir(remainFloor, targetFloor)) { // 같은 방향의 층이면
            if (n % w >= num % w) result++;
        } else { // 다른 방향의 층이면
            if (num % w == 0 || n % w + num % w > w) result++;
        }
        
        return result;
    }
    
    private static boolean isSameDir(int f1, int f2) {
        if (f1 % 2 == f2 % 2) return true;
        else return false;
    }
}