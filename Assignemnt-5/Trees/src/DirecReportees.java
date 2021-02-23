import java.util.*;

class Node{
    int data;
    Node left, right;
    public Node(int x){
        data = x;
        left = null;
        right = null;
    }
}

public class DirecReportees {
    public static void findWithBFS(Node root, int man){
        int left , right;
        left = -1;
        right = -1;
        if (root == null)
            return;
        Queue<Node> q = new LinkedList<Node>();
        q.add(root);
        while (!q.isEmpty()){
            Node curr = q.peek();
            q.remove();
            if (curr.data == man){
                if(curr.left != null)
                    left = curr.left.data;
                if (curr.right != null)
                    right = curr.right.data;
                break;
            }
            if (curr.left != null)
                q.add(curr.left);
            if (curr.right != null)
                q.add(curr.right);

        }
        System.out.println("Employees: " + left + " "+ right);
    }

    public static void findWithInorder(Node root, int data){
        if (root == null)
            return;
        findWithInorder(root.left, data);
        if (root.data == data){
            if (root.left != null)
                System.out.println(root.left.data + " ");
            else
                System.out.println(-1);
            if (root.right != null)
                System.out.println(root.right.data+" ");
            else
                System.out.println(-1);
            return;
        }
        findWithInorder(root.right, data);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.right = new Node(5);
        root.left.left = new Node(4);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        findWithBFS(root, 2);
        findWithInorder(root, 2);


    }
}
