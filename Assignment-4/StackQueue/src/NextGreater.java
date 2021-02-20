/*
Given an array, print the Next Greater Element (NGE)
for every element. The Next greater Element for an element x is the first greater element on the right side of x in the array.
Elements for which no greater element exist, consider next greater element as -1
 */
import java.util.Stack;
import java.util.Scanner;

public class NextGreater {
    static int[] printNGE(int arr[], int n){
        Stack<Integer> s = new Stack<>();
        int nge[] = new int[n];
        nge[n-1] = -1;
        s.push(arr[n-1]);

        for (int i = n-2; i>=0; i--){
            while ((!s.isEmpty()) && (s.peek() <= arr[i])){
                s.pop();
            }
            int ng = (s.isEmpty()) ? -1: s.peek();
            nge[i] = ng;
            s.push(arr[i]);
        }
        return nge;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i =0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        int nge[];
        nge = printNGE(arr, n);
        for(int i: nge){
            System.out.println(i);
        }

    }
}
