import java.util.*;
class Stack{
    static int MAX = 1000;
    int top;
    int a[] = new int[MAX];

    Stack(){
        this.top = -1;
    }
    boolean isEmpty(){
        return this.top < 0;
    }
    boolean push(int x){
        if (this.top >= (MAX - 1)){
            System.out.println("Stack Overflow");
            return false;
        }
        else{
            a[++top] = x;
            System.out.println(x + "pushed to stack");
            return true;
        }
    }
    int pop(){
        if (top < 0){
            System.out.println("Stack Underflow");
            return -1;
        }
        else{
            int x = a[top--];
            return x;
        }
    }
    int peek(){
        if (top < 0){
            System.out.println("Stack Underflow");
            return -1;
        }
        else{
            int x = a[top];
            return x;
        }
    }
}

class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
    }
}

class StackAsLList{
    Node head;
    StackAsLList(){
        head = null;
    }
    boolean isEmpty(){
        if (head == null)
            return true;
        else
            return false;
    }
    void push(int data){
        Node new_node = new Node(data);
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
}

public class StackImplementation {
    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.push(40);
        System.out.println(s.pop() + " Popped from stack");
        System.out.println(s.pop() + " Popped from stack\n");

        // implementing using linked list
        StackAsLList sl = new StackAsLList();
        sl.push(10);
        sl.push(20);
        sl.push(40);
        System.out.println(sl.pop() + " Popped from stack");
        System.out.println(sl.pop() + " Popped from stack\n");
    }

}
