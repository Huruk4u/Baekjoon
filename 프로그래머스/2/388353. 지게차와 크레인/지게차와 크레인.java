import java.util.*;
import java.io.*;


class Solution {

    private static int N, M;
    
    private static int[] dy = {-1, 1, 0, 0};
    
    private static int[] dx = {0, 0, -1, 1};
    
    private static char[][] matrix;
    
    private static char EMPTY = '\0';
    
    public int solution(String[] storage, String[] requests) {
        N = storage.length;
        M = storage[0].length();
        
        matrix = new char[N+2][M+2];
        for (int y = 1; y < N+1; y++) {
            for (int x = 1; x < M+1; x++) {
                matrix[y][x] = storage[y-1].charAt(x-1);
            }
        }
        
        for (String request: requests) {
            char token = request.charAt(0);
            
            if (request.length() == 2) {
                bruteForce(token);
            } else {
                Queue<Point> queue = new ArrayDeque();
                queue.add(new Point(0, 0));
                bfs(queue, token);
            }
            
            // System.out.println("----------------------------");
            // for (int y = 0; y < N+2; y++) {
            //     System.out.println(Arrays.toString(matrix[y]));
            // }
        }
        
        int result = 0;
        for (int y = 1; y < N+1; y++) {
            for (int x = 1; x < M+1; x++) {
                if (matrix[y][x] != EMPTY) result++;
            }
        }
        
        
        return result;
    }
    
    private static void bruteForce(char token) {
        for (int y = 1; y < N+1; y++) {
            for (int x = 1; x < M+1; x++) {
                if (matrix[y][x] == token) {
                    matrix[y][x] = EMPTY;
                }
            }
        }
        return;
    }
    
    private static void bfs(Queue<Point> queue, char token) {
        boolean[][] visited = new boolean[N+2][M+2];
        visited[queue.peek().y][queue.peek().x] = true;
        
        while (!queue.isEmpty()) {
            Point curr = queue.remove();
            
            // System.out.println(String.format("%d %d visited", curr.y, curr.x));
            
            for (int i = 0; i < 4; i++) {
                int ny = curr.y + dy[i];
                int nx = curr.x + dx[i];
                
                if (!inRange(ny, nx) || visited[ny][nx]) continue;
                
                if (matrix[ny][nx] != EMPTY) {
                    if (matrix[ny][nx] == token) {
                        visited[ny][nx] = true;
                        matrix[ny][nx] = EMPTY;
                    }
                } else {
                    visited[ny][nx] = true;
                    queue.add(new Point(ny, nx));
                }
            }
        }
        
        return;
    }
    
    private static boolean inRange(int y, int x) {
        return (0 <= y && y < N+2) && (0 <= x && x < M+2);
    }
    
    private static class Point {
        int y, x;
        
        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}