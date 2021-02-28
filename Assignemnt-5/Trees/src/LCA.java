import java.util.*;

public class LCA {
    static boolean findPath(Node root, int n, ArrayList<Integer> path){
        if (root == null)
            return false;
        path.add(root.data);
        if (root.data == n)
            return true;
        if (root.left != null && findPath(root.left, n, path)){
            return true;
        }
        if (root.right != null && findPath(root.right, n, path)){
            return true;
        }
        path.remove(path.size()-1);
        return false;
    }
    static int findLCA(Node root, int n1, int n2){
        if(root == null)
            return -1;
        if(root.data == n1 && root.data == n2)
            return root.data;
        ArrayList<Integer> path1 = new ArrayList<>();
        ArrayList<Integer> path2 = new ArrayList<>();

        if (!findPath(root, n1, path1) || !findPath(root, n2, path2)){
            return -1;
        }
        for (int i: path1)
            System.out.println(i);
        for (int i: path2)
            System.out.println(i);
        int i;
        for (i=0; i<path1.size() && i<path2.size(); i++){
            if (!path1.get(i).equals(path2.get(i)))
                break;
        }
        return path1.get(i-1);

    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.right = new Node(5);
        root.left.left = new Node(4);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        System.out.println("LCA(4,6) " + findLCA(root, 4, 6));

    }
}
