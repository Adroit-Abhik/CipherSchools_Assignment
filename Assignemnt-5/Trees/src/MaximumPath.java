import java.util.*;

public class MaximumPath {
    static int maxBetweenTwoLeaves = 0;
    public static int maxPathSum(Node node){
        if (node == null)
            return 0;
        if (node.left == null && node.right == null)
            return node.data;

        int l = maxPathSum(node.left);
        int r = maxPathSum(node.right);

        if (node.left != null && node.right != null){
            if (l + r + node.data > maxBetweenTwoLeaves){
                maxBetweenTwoLeaves = l + r + node.data;
            }
            return Math.max(l, r) + node.data;
        }
        return node.left != null ? 1+node.data : r + node.data;

    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.right = new Node(5);
        root.left.left = new Node(4);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        System.out.println(maxPathSum(root));
    }
}
