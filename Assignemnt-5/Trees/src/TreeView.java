import java.util.*;

public class TreeView {
    static int MAXLEVEL = 0;
    public static void LeftView(Node root){
        if (root == null)
            return;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()){
            int n = q.size();
            for (int i=0; i<n; i++){
                Node leftN = q.poll();
                if (i == 0)
                    System.out.print(leftN.data + " ");
                if (leftN.left != null)
                    q.add(leftN.left);
                if (leftN.right != null)
                    q.add(leftN.right);
            }
        }

    }

    public static void RightView(Node root, int level){
        if (root == null)
            return;
        if (MAXLEVEL < level) {
            System.out.println(root.data + " ");
            MAXLEVEL = level;
        }
        RightView(root.right, level+1);
        RightView(root.left, level+1);

    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.right = new Node(5);
        root.left.left = new Node(4);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        LeftView(root);
        System.out.println(" ");
        RightView(root, 1);
    }
}
