import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 좌료 정렬하기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Person[] p = new Person[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            p[i] = new Person(age, name);
        }

        Arrays.sort(p, (s1, s2) -> {
            return s1.age - s2.age;
        });

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(p[i].toString());
        }
        System.out.println(sb);
    }

    public static class Person {
        int age;
        String name;

        public Person(int age, String name) {
            this.age = age;
            this.name = name;
        }

        @Override
        public String toString() {
            return age + " " + name + "\n";
        }
    }
}