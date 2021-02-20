/*
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.
 */

import java.util.Stack;
import java.util.Scanner;

public class NearesSmallerLeft {
    public static void PSE(int arr[], int n){
        Stack<Integer> s = new Stack<>();
        s.push(arr[0]);
        int ifNoSE = -9999;
        System.out.println(ifNoSE + " ");
        for (int i=1; i<n; i++){
            while ((!s.isEmpty()) && (s.peek() >= arr[i])){
                s.pop();
            }
            int se = (s.isEmpty())? ifNoSE: s.peek();
            System.out.println(se + " ");
            s.push(arr[i]);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i =0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        PSE(arr, n);
    }
}
