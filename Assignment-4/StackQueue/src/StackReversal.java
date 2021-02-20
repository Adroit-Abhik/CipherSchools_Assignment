import java.util.Stack;

class StackNode{
    int data;
    StackNode next;
    public StackNode(int data){
        this.data = data;
        this.next = null;
    }
}

class StackWithReversal{
    StackNode head;
    StackWithReversal(){
        head = null;
    }
    boolean isEmpty(){
        if (head == null)
            return true;
        else
            return false;
    }
    void push(int data){
        StackNode new_node = new StackNode(data);
        new_node.next = head;
        head = new_node;
    }
    int pop(){
        if (head == null)
            return -1;
        int res = head.data;
        head = head.next;
        return res;
    }
    void reverse(){
        if (head == null)
            return;
        StackNode prev = null;
        StackNode curr = head;

        while (curr != null){
            StackNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
    }

}



public class StackReversal {
    public static void main(String[] args) {
        StackWithReversal s = new StackWithReversal();
        s.push(10);
        s.push(20);
        s.push(30);
        s.push(40);

        System.out.println(s.pop());
        s.reverse();
        System.out.println(s.pop());
    }
}
