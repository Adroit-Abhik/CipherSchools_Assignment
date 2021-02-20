import java.util.Stack;
import java.util.Scanner;



public class LargestAreaHistogram {
    public static int[] PSE(int arr[], int n){
        Stack<Integer> s = new Stack<>();
        s.push(0);
        int pse[] = new int[n];
        pse[0] = -1;
        for (int i=1; i<n; i++){
            while ((!s.isEmpty()) && (arr[s.peek()] > arr[i])){
                s.pop();
            }
            int se = (s.isEmpty())? -1: s.peek();
            pse[i] = se;
            //System.out.println(se);
            s.push(i);
        }
        return pse;
    }
    public static int[] NSE(int arr[], int n){
        Stack<Integer> s = new Stack<>();
        s.push(n-1);
        int nse[] = new int[n];
        nse[n-1] = n;
        for (int i=n-2; i>=0; i--) {
            while ((!s.isEmpty()) && (arr[s.peek()] > arr[i]))
                s.pop();
            int se = (s.isEmpty()) ? n : s.peek();
            nse[i] = se;
            //System.out.println(se);
            s.push(i);
        }
        return nse;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int hist[] = new int[n];
        for(int i =0; i<n; i++){
            hist[i] = sc.nextInt();
        }

        //int hist[] = { 6, 2, 5, 4, 5, 1, 6 };
        //int n = 7;

        int res = 0;
        int curr = 0;
        int pse[];
        int nse[];

        pse = PSE(hist, n);
        nse = NSE(hist, n);

        for(int i=0; i<n; i++){
            curr = hist[i];
            curr += (i - pse[i] - 1) * hist[i];
            curr += (nse[i] - i - 1) * hist[i];
            res = Math.max(res, curr);
        }
        System.out.println(res);

    }
}
