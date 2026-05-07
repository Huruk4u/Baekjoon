import java.util.*;
import java.io.*;

class Solution {
    
    private int[] agents;
    
    private List<Request>[] requests;
    
    private int K, N;
    
    private int answer;
    
    public int solution(int k, int n, int[][] reqs) {
        K = k;
        N = n;
        answer = 987654321;
        
        agents = new int[K+1];
        Arrays.fill(agents, 1);
        
        requests = new ArrayList[K+1];
        for (int i = 0; i < K+1; i++) requests[i] = new ArrayList();
        for (int[] req: reqs) requests[req[2]].add(new Request(req[0], req[1]));
        
        permutation(1, N);
        
        return answer;
    }
    
    private void permutation(int idx, int n) {
        if (idx == K+1) {
            int temp = 0;
            for (int i = 1; i < K+1; i++) temp += agents[i];
            
            if (temp == N) {
                int rtn = 0;
                // System.out.println(Arrays.toString(agents));
                for (int k = 1; k < K+1; k++) {
                    int waitingTime = simulation(requests[k], agents[k]);
                    // System.out.println(String.format("대기시간은 %d분", waitingTime));
                    rtn += waitingTime;
                }
                answer = Integer.min(answer, rtn);
            }
            return;
        }
        
        int maxRange = n - (K - idx - 1);
        for (int i = 1; i <= maxRange; i++) {
            agents[idx] = i;
            permutation(idx + 1, n - i);
        }
        return;
    }
    
    private int simulation(List<Request> request, int agent) {
        int waitingTime = 0;
        
        PriorityQueue<Integer> heap = new PriorityQueue();
        for (int i = 0; i < request.size(); i++) {
            Request curr = request.get(i); // 처리해야 하는 상담 요청
            if (agent - heap.size() <= 0) { // 가용 상담원의 수 - queue.size가 0이면
                int currTime = heap.remove(); // 종료시간이 가장 빠른걸 queue에서 하나 뺀다.
                
                // 뺐는데, 상담원의 종료 시간이 상담 요청의 도착시간보다 늦으면? 늦은만큼 대기시간 추가
                if (currTime > curr.arrivalTime) {
                    waitingTime += (currTime - curr.arrivalTime);
                    heap.add(currTime + curr.processTime);
                } else {
                    heap.add(curr.arrivalTime + curr.processTime);
                }
                
            } else {
                heap.add(curr.arrivalTime + curr.processTime);
            }
        }
        return waitingTime;
    }
    
    private class Request implements Comparable<Request> {
        int arrivalTime, processTime;
        
        Request(int arrivalTime, int processTime) {
            this.arrivalTime = arrivalTime;
            this.processTime = processTime;
        }
        
        @Override
        public int compareTo(Request other) {
            return Integer.compare(this.arrivalTime, other.arrivalTime);
        }
        
        @Override
        public String toString() {
            return String.format("(%d, %d)", this.arrivalTime, this.processTime);
        }
    }
}