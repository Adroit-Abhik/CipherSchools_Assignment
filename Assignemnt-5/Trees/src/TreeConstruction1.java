import java.util.*;


class TNode{
    char data;
    TNode left, right;
    public TNode(char x){
        data = x;
        left = null;
        right = null;
    }
}


public class TreeConstruction1 {
    static int preIdx = 0;

    public static TNode buildTree(char in[], char pre[], int startIdx, int endIdx){
        if (startIdx > endIdx)
            return null;
        TNode tNode = new TNode(pre[preIdx++]);
        // if this node is lead node
        if (startIdx == endIdx)
            return tNode;

        int inIdx = search(in, startIdx, endIdx, tNode.data);

        tNode.left = buildTree(in, pre, startIdx, inIdx-1);
        tNode.right = buildTree(in, pre, inIdx+1, endIdx);

        return tNode;
    }

    public static int search(char in[], int strt, int end, char val){
        int i;
        for (i = strt; i<end; i++){
            if (in[i] == val)
                return i;
        }
        return i;
    }

    public static void main(String[] args) {
        char in[] = new char[] { 'D', 'B', 'E', 'A', 'F', 'C' };
        char pre[] = new char[] { 'A', 'B', 'D', 'E', 'C', 'F' };
        int len = in.length;
        TNode root = buildTree(in, pre, 0, len-1);
    }
}
