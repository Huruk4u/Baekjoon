import java.util.*;

class Solution {
    
    private static int INF = 987654321;
    
    private static int TARGET;
    
    public int[] solution(int T) {
        
        TARGET = T;
        
        PriorityQueue<Node> heap = new PriorityQueue();
        heap.add(new Node(0, 0, 0));
        
        return dijkstra(heap);
    }
    
    private static int[] dijkstra(PriorityQueue<Node> heap) {
        
        Set<Integer> visited = new HashSet();
        
        while(!heap.isEmpty()) {
            Node curr = heap.remove();
            
            if (curr.score == TARGET) return new int[] {curr.cost, curr.hitSingleOrBull};
            
            if (visited.contains(curr.score)) continue;
            visited.add(curr.score);
            
            // System.out.println(curr);
            
            if (inRange(curr.score + 50)) {
                heap.add(new Node(curr.score + 50, curr.cost + 1, curr.hitSingleOrBull + 1));
            }
            
            for (int i = 1; i < 21; i++) {
                if (inRange(curr.score + i)) {
                    heap.add(new Node(curr.score + i, curr.cost + 1, curr.hitSingleOrBull + 1));
                }
                if (inRange(curr.score + i * 2)) {
                    heap.add(new Node(curr.score + i * 2, curr.cost + 1, curr.hitSingleOrBull));
                }
                if (inRange(curr.score + i * 3)) {
                    heap.add(new Node(curr.score + i * 3, curr.cost + 1, curr.hitSingleOrBull));
                }
            }
        }
        return new int[]{};
    }
    
    private static boolean inRange(int x) {
        return (0 <= x && x <= TARGET);
    }
    
    private static class Node implements Comparable<Node> {
        int score, cost, hitSingleOrBull;
        
        public Node(int score, int cost, int hitSingleOrBull) {
            this.score = score;
            this.cost = cost;
            this.hitSingleOrBull = hitSingleOrBull;
        }
        
        @Override
        public String toString() {
            return String.format("(%d, %d, %d)", score, cost, hitSingleOrBull);
        }
        
        @Override
        public int compareTo(Node other) {
            if (this.cost != other.cost) return this.cost - other.cost;
            return other.hitSingleOrBull - this.hitSingleOrBull;
        }
    }
}