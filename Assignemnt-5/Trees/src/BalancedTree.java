import java.awt.*;
import java.util.*;


public class BalancedTree {
    public static int height(Node root){
        if (root == null)
            return 0;
        else
            return Math.max(height(root.left), height(root.right)) + 1;
    }
    public static boolean isBalancedNaive(Node root){
        if (root == null)
            return true;
        int lh = height(root.left);
        int rh = height(root.right);
        return (Math.abs(lh-rh) <= 1 && isBalancedNaive(root.left) && isBalancedNaive(root.right));
    }

    public static int isBalancedFaster(Node root){
        /*
        Idea is to find the height in the same function.
        Call for left and right subtree.
        if any subtrre returns -1 then return -1 for the entire tree.
        else if balanced return height for each subtree
         */
        if (root == null){
            // leaf node height = 0
            return 0;
        }
        int lh = isBalancedFaster(root.left);
        if (lh == -1)
            return -1;
        int rh = isBalancedFaster(root.right);
        if (rh == -1)
            return -1;
        // if left and right sub tree are balanced then return height else -1
        if (Math.abs(lh - rh) > 1)
            return -1;
        else
            return Math.max(lh, rh) + 1;
    }



    public static void main(String[] args) {
        Node root=new Node(10);
        root.left=new Node(5);
        root.right=new Node(30);
        root.right.left=new Node(15);
        root.right.right=new Node(20);

        System.out.println(isBalancedNaive(root));
        System.out.println(isBalancedFaster(root));

    }
}
