import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


class Solution
{
	public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int t=1; t<=10; t++){
            int dump = Integer.parseInt(br.readLine());

            int[] arr = new int[100];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i=0; i<100; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }

            for(int i=0; i<dump; i++){
                Arrays.sort(arr);
                arr[0]++;
                arr[99]--;
            }
            Arrays.sort(arr);
            int result = arr[99] - arr[0];
            System.out.println("#" + t + " " + result);
        }
    }
}