import java.io.*;
import java.util.*;


class Solution {

    private int N;
    
    private List<Edge>[] graph;
    
    private int INF = 987654321;
    
    public int solution(int N, int[][] edges, int K) {
        this.N = N;
        
        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList();
        
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));
        }
        
        PriorityQueue<State> heap = new PriorityQueue();
        heap.add(new State(1, 0));
        int[] dist = dijkstra(heap);
        
        int answer = 0;
        for (int i = 1; i < N+1; i++) {
            if (dist[i] <= K) answer++;
        }
        
        return answer;
    }
    
    private int[] dijkstra(PriorityQueue<State> heap) {
        int[] dist = new int[N+1];
        Arrays.fill(dist, INF);
        dist[1] = 0;
        
        while (!heap.isEmpty()) {
            State curr = heap.remove();
            if (dist[curr.number] < curr.cost) continue;
            
            for (Edge next: graph[curr.number]) {
                if (dist[next.number] <= dist[curr.number] + next.weight) continue;
                dist[next.number] = dist[curr.number] + next.weight;
                heap.add(new State(next.number, dist[next.number]));
            }
        }
        
        return dist;
    }
    
    private class Edge {
        int number, weight;
        
        Edge(int number, int weight) {
            this.number = number;
            this.weight = weight;
        }
    }
    
    private class State implements Comparable<State> {
        int number, cost;
        
        State(int number, int cost) {
            this.number = number;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(State other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
}