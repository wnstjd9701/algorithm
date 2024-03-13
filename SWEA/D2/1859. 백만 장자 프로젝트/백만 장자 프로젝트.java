import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception, NullPointerException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int N = Integer.parseInt(br.readLine());
            int[] price = new int[N];
            st = new StringTokenizer(br.readLine(), " ");
            for(int i=0; st.hasMoreTokens(); i++){
                price[i] = Integer.parseInt(st.nextToken());
            }
            int length = price.length;
            int maxValue = price[N-1];
            long result = 0;

            for(int i=N-1; i>=0; i--){
                if(price[i] > maxValue) maxValue = price[i];
                result += maxValue-price[i];
            }
            System.out.println("#" + test_case + " " + result);
        }
    }
}
