import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim());

        List<Computer>[] computers = new ArrayList[N+1];
        for (int i = 1; i < N+1; i++) computers[i] = new ArrayList();

        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int c = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            computers[c].add(new Computer(i, t));
        }

        // i번째 컴퓨터의 프로세스 시작, 종료 시간
        int[] start = new int[N+1];
        int[] end = new int[N+1];
        for (int currClass = 1; currClass < N; currClass++) {
            for (Computer currComputer : computers[currClass]) {
                for (Computer nextComputer : computers[currClass + 1]) {
                    int weight = currComputer.processTime + (currComputer.number - nextComputer.number) * (currComputer.number - nextComputer.number);
                    start[nextComputer.number] = Integer.max(start[nextComputer.number], start[currComputer.number] + weight);
                    end[nextComputer.number] = Integer.max(end[nextComputer.number], start[nextComputer.number] + nextComputer.processTime);
                }
            }
        }

        int answer = 0;
        for (int i = 1; i < N+1; i++) answer = Integer.max(answer, end[i]);

        System.out.println(answer);

        br.close();
    }

    private static class Computer {
        int number, processTime;
        public Computer(int number, int processTime) {
            this.number = number;
            this.processTime = processTime;
        }
    }
}
