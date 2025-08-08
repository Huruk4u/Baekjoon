import java.util.*;

class Solution {
    
    private static List<Integer>[] graph;
    
    private static int INF = 987654321;
    
    private static int[][] dp;
    
    public int solution(int N, int[][] edges) {
        
        // graph 생성
        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();

        for (int i = 0; i < N-1; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            
            graph[u].add(v);
            graph[v].add(u);
        }
        
        // dp 초기값 세팅
        dp = new int[N+1][2];
        for (int i = 0; i < N+1; i++) Arrays.fill(dp[i], INF);
        
        return Integer.min(dfs(1, 0, 0), dfs(1, 1, 0));
    }
    
    private static int dfs(int curr, int lightOn, int parent) {
        // 이미 방문한 적이 있다면 그대로 return
        if (dp[curr][lightOn] != INF) return dp[curr][lightOn];
        
        // System.out.println(String.format("%d %d visited", curr, lightOn));
        
        int temp = 0;
        for (int next : graph[curr]) {
            if (next == parent) continue;
            // 현재 등대의 불을 끄는 경우
            if (lightOn == 0) {
                temp += dfs(next, 1, curr);
            } else {
                temp += Integer.min(dfs(next, 0, curr), dfs(next, 1, curr));
            }
        }
        
        if (lightOn == 1) dp[curr][lightOn] = temp+1;
        else dp[curr][lightOn] = temp;
        
        return dp[curr][lightOn];
    }
}